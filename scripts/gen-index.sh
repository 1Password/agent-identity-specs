#!/usr/bin/env bash
# Generate the GitHub Pages landing page listing every built draft.
# Lists each draft-*.html found in the current directory (with Text/XML links).
set -euo pipefail

cat <<'HEAD'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>1Password Agent Identity Spec Drafts</title>
<link rel="stylesheet" href="assets/1password.css">
<style>body{max-width:48rem;margin:3rem auto;padding:0 1rem;font-family:system-ui,sans-serif;line-height:1.5}ul{padding-left:0;list-style:none}li{margin:1.25rem 0}.formats a{margin-right:.5rem}</style>
</head>
<body>
<h1>1Password Agent Identity Spec Drafts</h1>
<ul>
HEAD

for d in $(ls draft-*.html | sed 's/\.html$//' | sort -u); do
  printf '  <li><a href="%s.html"><strong>%s</strong></a><div class="formats"><a href="%s.html">HTML</a> · <a href="%s.txt">Text</a> · <a href="%s.xml">XML</a></div></li>\n' "$d" "$d" "$d" "$d" "$d"
done

cat <<'FOOT'
</ul>
</body>
</html>
FOOT
