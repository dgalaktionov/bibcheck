# bibcheck
A script to check references from a BibTeX file against Google Scholar

## Backstory
Once there was a reviewer who complained about typos in researcher names from the references. He was wrong, but that was enough to have a thesis advisor on my ass asking me to re-check every reference.

So I could search them all one by one in Google Scholar and checking manually that the titles, names and journales/proceedings match 100%...

Or I could automate that boring task. So I needed bibcheck.

## Installation
`pip3 install git+https://github.com/dgalaktionov/bibcheck.git`

## Usage
`bibcheck.py <file.bib>`

When no file specified, it will read from the stdin.

So the input is a collection of BibTeX entries. Every entry is queried against Google Scholar and the result is printed to stdout in BibTeX format. That way I can `bibcheck.py paper.bib > scholar.bib`, and then compare the contents of `paper.bib` and `scholar.bib` using kdiff3 or whatever comparing tool I have at hand.

If I see the need, I may implement some fancy automatic comparison, displaying information only about the mismatched entries.
