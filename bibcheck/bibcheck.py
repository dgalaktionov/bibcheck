#!/usr/bin/env python3

import scholar
import bibtexparser
import sys
import subprocess
import time

def find_bibtex(entry):
	proc = None

	if "doi" in entry:
		proc = subprocess.Popen(["scholar.py", "-c", "1", "-A", entry["doi"], "--citation", "bt"], stdout=subprocess.PIPE, universal_newlines=True)
	else:
		cmd = ["scholar.py", "-c", "1"]

		if "title" in entry:
			cmd.extend(["-p", entry["title"], "-t"])

		if "author" in entry:
			#cmd.extend(["-a", entry["author"]])
			#FIXME
			pass

		if "year" in entry:
			cmd.extend(["--after", entry["year"], "--before", entry["year"]])

		cmd.extend(["--citation", "bt"])

		#print(" ".join(cmd))

		if len(cmd) == 3:
			print("Could not get enough selectors for %s" % entry["ID"], file=sys.stderr)
		else:
			proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)

	if proc:
		return str(proc.stdout.read())
	else:
		return "ERRNOPROC"

def main(argv):
	if (len(argv) < 2):
		bibtex_str = sys.stdin.read()
	else:
		try:
			with open(argv[1]) as bibtex_file:
				bibtex_str = bibtex_file.read()
		except OSError:
			print("Could not read file. Does it exist?", file=sys.stderr)
			return 1
	
	parser = bibtexparser.bparser.BibTexParser(common_strings=True)
	bib_db = parser.parse(bibtex_str)

	writer = bibtexparser.bwriter.BibTexWriter()

	for entry in bib_db.entries:
		print(find_bibtex(entry))
		time.sleep(5) # To (hopefully) conform with usage rates

	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))