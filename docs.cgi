#!/usr/bin/python

#################################

docpath = "/var/www/html/itensor/docs/"
reldocpath = "docs/"
header_fname = "docs_header.html"
footer_fname = "docs_footer.html"

#################################

import re
named_link_re = re.compile("(.+?)\|(.+)")
arxiv_link_re = re.compile("(.+?)\|(.+)")

import cgitb
cgitb.enable()

from cgi import FieldStorage
form = FieldStorage()

def fileExists(fname):
    try:
        return open(fname)
    except IOError:
        return None

def printContentType():
    print "Content-Type: text/html\n\n"

def convert(string):
    #Convert arxiv:####.#### links
    string = re.sub(r"arxiv:(\d\d\d\d\.\d\d\d\d)",r"arxiv:<a href='http://arxiv.org/abs/\1'>\1</a>",string)
    slist = re.split("\[\[(.+?)\]\]",string)
    mdstring = slist[0]
    for j in range(1,len(slist)):
        chunk = slist[j]
        if j%2 == 0:
            mdstring += chunk
        else:
            nlmatch = named_link_re.match(chunk)
            if nlmatch:
                name = nlmatch.group(1)
                link = nlmatch.group(2)
                mdstring += "[%s](docs.cgi?page=%s)"%(name,link)
            else:
                mdstring += "[%s](docs.cgi?page=%s)"%(chunk,chunk)

    import markdown2
    return markdown2.markdown(mdstring)

page = form.getvalue("page")

if page == None: page = "main"

mdfname = reldocpath + page + ".md"
mdfile = fileExists(mdfname)

bodyhtml = ""
if mdfile:
    bodyhtml = convert("".join(mdfile.readlines()))
    mdfile.close()
else:
    bodyhtml = "<p>(Documentation file not found)</p>"

printContentType()
header_file = open(header_fname)
footer_file = open(footer_fname)
print "".join(header_file.readlines())
print bodyhtml
print "".join(footer_file.readlines())
footer_file.close()
header_file.close()
