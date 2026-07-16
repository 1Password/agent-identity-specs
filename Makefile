DRAFTS := \
	draft-1password-agent-identity-local-delegated

XML  := $(addsuffix .xml,  $(DRAFTS))
HTML := $(addsuffix .html, $(DRAFTS))
TXT  := $(addsuffix .txt,  $(DRAFTS))

.PHONY: all xml html txt lint clean

all: html txt

xml:  $(XML)
html: $(HTML)
txt:  $(TXT)

%.xml: %.md
	kdrfc -3 -x $<

%.html: %.xml assets/1password.css
	xml2rfc --html --allow-local-file-access $<
	@# Inject the 1Password branding stylesheet before </head>.
	@sed -i.bak 's|</head>|<link rel="stylesheet" href="assets/1password.css"></head>|' $@ && rm -f $@.bak
	@# Replace @@IMG:path@@ ascii-art markers with <img> tags. Temporary; remove
	@# once raster diagrams are converted to RFC-7996-compliant SVG.
	@perl -i -0pe 's|<pre>\s*\@\@IMG:([^\@\s]+)\@\@\s*</pre>|<img src="$$1" alt="(diagram)" style="max-width:100%;height:auto"/>|g' $@
	@# Inject a per-draft body class so CSS can apply draft-specific palette.
	@if echo "$@" | grep -q local-delegated; then \
	  perl -i -pe 's|<body class="xml2rfc"|<body class="xml2rfc draft-local-delegated"|' $@; \
	fi
	@# Strip auto-generated Authors' Addresses section (we render colophon instead).
	@perl -i -0pe 's|<div id="authors-addresses">.*?</section>\s*</div>||gs' $@
	@perl -i -0pe 's|<li[^>]*>\s*<p[^>]*><a[^>]*></a><a href="#name-authors-addresses"[^>]*>[^<]+</a></p>\s*</li>||gs' $@
	@# Reorder back-matter: Acknowledgments (13) -> Normative (14) -> Informative (15) -> About.
	@python3 scripts/reorder-back.py $@

%.txt: %.xml
	xml2rfc --text --allow-local-file-access $<

lint: $(TXT)
	@for f in $(TXT); do idnits --verbose $$f; done

clean:
	rm -f $(XML) $(HTML) $(TXT) $(addsuffix .html.bak, $(DRAFTS))
	rm -rf _site
