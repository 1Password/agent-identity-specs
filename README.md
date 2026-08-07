# Local Delegated Agent Identity Architecture

Source repository for the Internet-Draft
**draft-1password-agent-identity-local-delegated**, Part 1 of the
1Password Agent Identity Series.

The canonical source is the kramdown-rfc Markdown file
[draft-1password-agent-identity-local-delegated.md](draft-1password-agent-identity-local-delegated.md).
Build outputs (`.xml`, `.html`, `.txt`) are generated from it and are
not checked in.

## Building locally

You need Ruby (for `kramdown-rfc`) and Python (for `xml2rfc`):

```sh
brew install ruby
gem install kramdown-rfc

brew install python
pip3 install xml2rfc
```

Then:

```sh
make            # build .html and .txt
make xml        # build .xml only
make lint       # run idnits on the .txt output (requires idnits)
make clean
```

## Repository layout

| Path                                                       | Purpose                                                              |
| ---------------------------------------------------------- | -------------------------------------------------------------------- |
| `draft-1password-agent-identity-local-delegated.md`        | Canonical source, written in kramdown-rfc Markdown.                  |
| `Makefile`                                                 | Builds `.xml` / `.html` / `.txt` via `kdrfc` and `xml2rfc`.          |
| `.github/workflows/build.yml`                              | CI: builds on every push/PR; publishes `main` to GitHub Pages.       |

## Publishing

CI on `main` deploys the rendered HTML to GitHub Pages. To enable
this:

1. In **Settings -> Pages**, set the source to **GitHub Actions**.
2. Push to `main`.

The deployed URL will be of the form
`https://<owner>.github.io/<repo>/`. Update the *About This
Document* boilerplate in the draft once the URL is known.

## Working on the draft

* Edit `draft-1password-agent-identity-local-delegated.md`.
* Run `make` and check the `.html` / `.txt` outputs look right.
* Commit only the Markdown source; build outputs are git-ignored.

When cutting a new revision (`-00` -> `-01`, etc.), bump the
`docname:` value in the front matter and rebuild.

## Submission to the IETF Datatracker

The `.xml` produced by `make xml` is the file you upload to
<https://datatracker.ietf.org/>. Before submission run `make lint`
and fix any `idnits` warnings.

For more advanced workflows (versioned drafts, diffs between
revisions, automatic submission), consider adopting
[martinthomson/i-d-template](https://github.com/martinthomson/i-d-template),
which is the de facto standard scaffolding for IETF drafts.

## Series

This document is Part 1 of a planned series on agent identity
architectures.

It also references the companion *OS-Level Workload Attestation* draft
(`draft-1password-os-level-workload-attestation`), which is currently
unpublished and coming soon, for the WIB verification protocol details.
