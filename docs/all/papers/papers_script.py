#!/usr/local/opt/python/libexec/bin/python
import arxiv
import sys
from os.path import exists

infile = None
if len(sys.argv) < 2:
    print("Usage: py papers_script.py input_file")

lines = []
for n in range(1,len(sys.argv)):
    infile = sys.argv[n]
    if exists(infile):
        f = open(infile,'r')
        lines = lines + f.readlines()
    else:
        lines = lines + [infile]

for line in lines:
    eprint = line.rstrip()
    search = arxiv.Search(id_list=[line])
    paper = next(search.results())
    title = paper.title
    authors = ""
    for a in paper.authors:
        authors += " " + str(a) + ", "

    url = ""
    if paper.doi != None:
        url = "https://doi.org/" + paper.doi
    else:
        url = "https://arxiv.org/abs/" + eprint
    if paper.journal_ref != None:
        print(f"* [{title}]({url}), {authors} <i style=\"color:#CC0000;\">{paper.journal_ref}</i>, arxiv:{eprint}\n")
    else:
        print(f"* [{title}](https://arxiv.org/abs/{eprint}), {authors} arxiv:{eprint}\n")

