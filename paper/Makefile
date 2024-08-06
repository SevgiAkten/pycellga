clean: paper.pdf
	rm paper.pdf

all: paper.md paper.bib
	pandoc -o paper.pdf paper.bib --citeproc
