#!/usr/bin/env python3
# Post-process the rendered HTML to reorder back-matter as:
#   13. Acknowledgments
#   14. Normative References
#   15. Informative References
#   About This Document  (unnumbered colophon)
# RFC 7991 schema requires <references> before <section> in <back> and
# treats numbered back-matter <section>s as "Appendix A/B/..." rather than
# continuing the body section count, so this rearrangement is HTML-only.
import re
import sys

path = sys.argv[1]
with open(path) as f:
    h = f.read()

def grab(pattern, text, flags=re.DOTALL):
    m = re.search(pattern, text, flags)
    return m.group(0) if m else None

def slice_div(text, start_marker, end_marker):
    """Return the substring from `start_marker` up to (but not including) the
       next `end_marker`. Returns None if either marker not found."""
    s = text.find(start_marker)
    if s == -1:
        return None
    e = text.find(end_marker, s)
    if e == -1:
        return None
    return text[s:e]

# Use positional slices to handle nested <section> inside the combined-references parent.
parent_refs_block = slice_div(h, '<div id="sec-combined-references">', '<div id="acknowledgments">')
norm_block = grab(
    r'<div id="sec-normative-references">\s*<section id="section-13\.1">.*?</section>\s*</div>', h)
inf_block = grab(
    r'<div id="sec-informative-references">\s*<section id="section-13\.2">.*?</section>\s*</div>', h)
ack_block = grab(
    r'<div id="acknowledgments">\s*<section[^>]*>.*?</section>\s*</div>', h)
about_block = grab(
    r'<div id="about-this-document">\s*<section[^>]*>.*?</section>\s*</div>', h)

if not all([parent_refs_block, norm_block, inf_block, ack_block, about_block]):
    sys.exit(0)

# Renumber Acknowledgments: add "13. " to its h2
ack_new = re.sub(
    r'(<h2 id="name-acknowledgments"[^>]*>\s*)(<a[^>]*class="section-name selfRef"[^>]*>)',
    r'\1<a href="#name-acknowledgments" class="section-number selfRef">13. </a>\2',
    ack_block, count=1)

# Promote Normative refs to "14." top-level h2
norm_new = norm_block
# Promote h3 -> h2, change selfRef numbering
norm_new = re.sub(
    r'<h3 id="name-normative-references">\s*<a href="#section-13\.1"[^>]*>\s*13\.1\.\s*</a>',
    r'<h2 id="name-normative-references"><a href="#name-normative-references" class="section-number selfRef">14. </a>',
    norm_new, count=1)
norm_new = re.sub(r'</h3>', '</h2>', norm_new, count=1)

# Promote Informative refs to "15."
inf_new = inf_block
inf_new = re.sub(
    r'<h3 id="name-informative-references">\s*<a href="#section-13\.2"[^>]*>\s*13\.2\.\s*</a>',
    r'<h2 id="name-informative-references"><a href="#name-informative-references" class="section-number selfRef">15. </a>',
    inf_new, count=1)
inf_new = re.sub(r'</h3>', '</h2>', inf_new, count=1)

# Splice: remove all five blocks from their existing positions, then insert in new order
# at the place where parent_refs_block was.
new_chunk = ack_new + '\n' + norm_new + '\n' + inf_new + '\n' + about_block

new_h = h
# Remove all five from current positions
for b in [parent_refs_block, ack_block, about_block]:
    new_h = new_h.replace(b, '', 1)
# Insert new_chunk at the position the parent_refs was originally located (which was first).
# The parent's removal left an empty hole; we'll insert the chunk before </body>.
new_h = re.sub(r'(?=</body>)', new_chunk + '\n', new_h, count=1)

# Update the TOC entries to match the new numbering & order
# TOC currently shows: "13. References", "13.1. Normative", "13.2. Informative",
# "Appendix A. Acknowledgments" (but Acknowledgments was unnumbered so just "Acknowledgments"),
# "About This Document"
# We want: "13. Acknowledgments", "14. Normative", "15. Informative", "About This Document"
# Find the TOC parent <ul> after </h2> "Table of Contents" — but simpler: just rewrite the
# specific TOC list items by their #name-X anchors.

# Replace TOC link for normative refs
new_h = re.sub(
    r'(<a href="#section-13\.1"[^>]*class="auto internal xref"[^>]*>)13\.1(</a>)',
    r'<a href="#name-normative-references" class="auto internal xref">14\2', new_h)
new_h = re.sub(
    r'(<a href="#section-13\.2"[^>]*class="auto internal xref"[^>]*>)13\.2(</a>)',
    r'<a href="#name-informative-references" class="auto internal xref">15\2', new_h)
# Acknowledgments TOC: it's currently unnumbered. Prefix "13. " and strip the
# empty <a href="#appendix-A"> stub xml2rfc emits (it renders as a stray gap
# that misaligns "13." relative to the "14." / "15." entries below).
new_h = re.sub(
    r'<a href="#appendix-A"[^>]*></a>(<a href="#name-acknowledgments" class="internal xref">)Acknowledgments(</a>)',
    r'<a href="#name-acknowledgments" class="auto internal xref">13</a>.  \1Acknowledgments\2',
    new_h, count=1)
# Remove "13. References" parent TOC entry (since we unwrap it)
new_h = re.sub(
    r'<li[^>]*>\s*<p[^>]*>\s*<a href="#section-13"[^>]*>13</a>\.\s*<a href="#name-references"[^>]*>References</a>\s*</p>\s*<ul[^>]*>(.*?)</ul>\s*</li>',
    r'\1', new_h, flags=re.DOTALL)

# Move the Acknowledgments TOC <li> above the Normative References <li> so the
# sidebar reads 13 -> 14 -> 15 (matches the reordered body). xml2rfc emits the
# TOC in source order, and our renumbering above only rewrites link text.
ack_toc_re = re.compile(
    r'\s*<li[^>]*class="[^"]*toc[^"]*"[^>]*>\s*<p[^>]*>(?:(?!</p>).)*?'
    r'<a href="#name-acknowledgments"[^>]*>Acknowledgments</a>\s*</p>\s*</li>',
    re.DOTALL,
)
m = ack_toc_re.search(new_h)
if m:
    ack_toc_li = m.group(0)
    new_h = new_h.replace(ack_toc_li, '', 1)
    new_h = re.sub(
        r'(<li[^>]*class="[^"]*toc[^"]*"[^>]*>\s*<p[^>]*>\s*<a href="#name-normative-references")',
        lambda mo: ack_toc_li.lstrip('\n') + '\n              ' + mo.group(1),
        new_h, count=1)

with open(path, 'w') as f:
    f.write(new_h)
