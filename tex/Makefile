.PHONY: all clean

all:
	$(MAKE) clean
	pdflatex --shell-escape thesis.tex && \
	biber thesis && \
	pdflatex --shell-escape thesis.tex && \
	pdflatex --shell-escape thesis

clean:
	rm -f thesis.aux thesis.bbl thesis.bcf thesis.out
	rm -f thesis.blg thesis.dvi thesis.log thesis.toc
	rm -f thesis.run.xml

