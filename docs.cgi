#!/usr/bin/python

#################################

docpath = "/var/www/html/itensor/docs/"
reldocpath = "docs/"
header_fname = "docs_header.html"
footer_fname = "docs_footer.html"

#################################

import re
named_link_re = re.compile("(.+?)\|(.+)")
#code_block_re = re.compile(r"<code>\n+(.+?)</code>",flags=re.DOTALL)
#paragraph_code_re = re.compile(r"<p><code>(.+?)</code></p>",flags=re.DOTALL)

#import cgitb
#cgitb.enable()

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
    #Convert cond-mat/####### links
    string = re.sub(r"cond-mat/(\d\d\d\d\d\d\d)",r"cond-mat/<a href='http://arxiv.org/abs/cond-mat/\1'>\1</a>",string)

    #Convert wiki links to markdownl link syntax
    slist = re.split("\[\[(.+?)\]\]",string)
    mdstring = slist[0]
    for j in range(1,len(slist)):
        chunk = slist[j]
        if j%2 == 0:
            mdstring += chunk
        else:
            #Check if a name is provided for this link
            nlmatch = named_link_re.match(chunk)
            if nlmatch:
                name = nlmatch.group(1)
                link = nlmatch.group(2)
                #mdstring += "<img src='link_arrow.png' class='arrow'/>[%s](docs.cgi?page=%s)"%(name,link)
                mdstring += "[%s](docs.cgi?page=%s)"%(name,link)
            else:
                #Otherwise use the raw link name (file -> file.md)
                mdstring += "[%s](docs.cgi?page=%s)"%(chunk,chunk)
                #mdstring += "<img src='link_arrow.png' class='arrow'/>[%s](docs.cgi?page=%s)"%(chunk,chunk)

    #Code below not needed: just indent 4 spaces and Markdown
    #will apply the <pre> tag which preserves formatting.
    #
    #Format code blocks, preserving newlines and indentation
    #slist = code_block_re.split(mdstring)
    #mdstring = slist[0]
    #for j in range(1,len(slist)):
    #    chunk = slist[j]
    #    last = False
    #    if j == (len(slist)-1): last = True
    #    if j%2 == 0: mdstring += chunk
    #    else: 
    #        #Convert whitespace to &nbsp; (html for non-breaking space)
    #        #chunk = re.sub(r"[ \t]",r"&nbsp;",chunk)
    #        #Convert < and > signs
    #        #chunk = re.sub(r"<",r"&lt;",chunk)
    #        #chunk = re.sub(r">",r"&gt;",chunk)
    #        #Convert newlines to </br>
    #        if not last:
    #            chunk = re.sub(r"\n",r"</br>\n",chunk)
    #
    #        mdstring += "<code>\n"+chunk+"</code>\n"

    #Convert markdown to html
    import markdown2
    htmlstring = markdown2.markdown(mdstring,extras=["fenced-code-blocks"])

    #Put in a special class for paragraphs that consist entirely of code
    #htmlstring = paragraph_code_re.sub(r"<p><div class='codeblock'>\1</div></p>",htmlstring)

    return htmlstring

page = form.getvalue("page")

if page == None: page = "main"

mdfname = reldocpath + page + ".md"
mdfile = fileExists(mdfname)

printContentType()

bodyhtml = ""
if mdfile:
    bodyhtml = convert("".join(mdfile.readlines()))
    mdfile.close()
else:
    bodyhtml = "<p>(Documentation file not found)</p>"

header_file = open(header_fname)
footer_file = open(footer_fname)
print "".join(header_file.readlines())
print bodyhtml
print "".join(footer_file.readlines())
footer_file.close()
header_file.close()
