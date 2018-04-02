from setuptools import setup

setup(name='bibcheck',
	version='0.3',
	description='Checks entries from a BibTeX file against Google Scholar API to find inaccurate references',
	url='http://github.com/dgalaktionov/bibcheck',
	author='DaGal',
	author_email='galaktionov@gmail.com',
	license='MIT',
	packages=['bibcheck'],
	install_requires=[
		"scholar==0.2",
		"bibtexparser"
	],
	dependency_links=[
		"https://github.com/dgalaktionov/scholar.py/tarball/master#egg=scholar-0.2"
	],
	scripts=[
		"bibcheck/bibcheck.py"
	],
	zip_safe=False)
