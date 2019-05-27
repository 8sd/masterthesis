.PHONY: all html clean

SOURCES := $(wildcard md/??_*.md)

all: lit resources pdf html

commit: lit
	git commit literatur

# PDF Targets

pdf: tex/contents/abstract.tex tex/contents/body.tex tex/resources
	$(MAKE) -C tex all

tex/contents/%.tex: md/%.md
	pandoc -f markdown -t latex -o $@ $<

# HTML Targets

html: html/md/abstract.md html/md/body.md html/resources

html/md/%.md: md/%.md
	cp $< $@

# General Targets

resources: md/resources
	cp md/resources/* tex/resources/
	cp md/resources/* html/resources/

md/body.md: $(SOURCES)
	cat md/??_*.md > md/body.md

lit: Literatur
	ls Literatur > literatur

clean:
	rm -f thesis.pdf md/body.md tex/contents/abstract.tex tex/contents/body.tex tex/resources/*
	rm -f html/md/* html/resources/*
	$(MAKE) -C tex clean