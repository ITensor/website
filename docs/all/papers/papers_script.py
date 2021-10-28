import arxiv
import sys


infile = None
if len(sys.argv) < 2:
    print("Usage: py papers_script.py input_file")
else:
    infile = sys.argv[1]

f = open(infile, 'r')
lines = f.readlines()

for line in lines:
    eprint = line.rstrip()
    search = arxiv.Search(id_list=[line])
    paper = next(search.results())
    title = paper.title
    authors = ""
    for a in paper.authors:
        authors += " " + str(a) + ", "
    print(f"* [{title}](https://arxiv.org/abs/{eprint}), {authors}arxiv:{eprint}\n")
