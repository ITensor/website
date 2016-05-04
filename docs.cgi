#!/usr/local/bin/python2.7

import sys
import re #regular expressions
from cgi import FieldStorage
#import markdown2
#import markdown

import mistune #Markdown renderer
from pygments import highlight
from pygments.lexers import CppLexer
from pygments.formatters import HtmlFormatter

from functools import partial
# Turn on cgitb to get nice debugging output.
# Remember to turn off when done debugging, otherwise not secure.
#import cgitb; cgitb.enable()

#################################

docpath = "/var/www/html/itensor/docs/"
reldocpath = "docs/"
prenav_header_fname = "docs_header_prenav.html"
postnav_header_fname = "docs_header_postnav.html"
footer_fname = "docs_footer.html"
this_fname = "docs.cgi"
nav_delimiter = "&nbsp;/&nbsp;"

#################################

sys.path.append("/opt/itensor.org/")

class MyRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        lexer = CppLexer()
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)

named_link_re = re.compile("(.+?)\|(.+)")
#code_block_re = re.compile(r"<code>\n+(.+?)</code>",flags=re.DOTALL)
#paragraph_code_re = re.compile(r"<p><code>(.+?)</code></p>",flags=re.DOTALL)

form = FieldStorage()

def fileExists(fname):
    try:
        open(fname)
        return True
    except IOError:
        return False

def openFile(fname):
    try:
        return open(fname)
    except IOError:
        return None

def printContentType():
    print "Content-Type: text/html\n\n"

def processMathJax(matchobj,delimit=""):
    math = re.sub(r"\\_","_",matchobj.group(0))
    if delimit=="@@":
        return "<span> " + math + " </span>"
    elif delimit=="$$":
        return "<div>\n" + math + "\n</div>\n<!---->"
    elif delimit=="align":
        return "<div>\n " + math + "\n</div>\n<!---->"
    return None

def includeFile(matchobj):
    spacing = len(matchobj.group(1))
    fname = matchobj.group(2)
    text = ""
    try:
        f = open(fname,'r')
        white = " "*spacing
        for line in f:
            text += white+line
        return text
    except:
        return "&lt;File {} not found&gt;".format(fname)
    

def convert(string):
    #Convert arxiv:####.#### links
    string = re.sub(r"arxiv:(\d\d\d\d\.\d+)",r"arxiv:<a target='_blank' href='http://arxiv.org/abs/\1'>\1</a>",string)
    #Convert cond-mat/####### links
    string = re.sub(r"cond-mat/(\d\d\d\d\d\d\d)",r"<a target='_blank' href='http://arxiv.org/abs/cond-mat/\1'>cond-mat/\1</a>",string)
    #Convert github:<sha> links
    string = re.sub(r"github:(\w{5})\w*",r"<a class='github' target='_blank' href='https://github.com/ITensor/ITensor/commit/\1'>\1</a>",string)
    #Convert #nn github issue links
    string = re.sub(r"issue #(\d+)",r"issue <a target='_blank' href='https://github.com/ITensor/ITensor/pull/\1'>#\1</a>",string)
    string = re.sub(r"bug #(\d+)",r"bug <a target='_blank' href='https://github.com/ITensor/ITensor/pull/\1'>#\1</a>",string)
    string = re.sub(r"request #(\d+)",r"request <a target='_blank' href='https://github.com/ITensor/ITensor/pull/\1'>#\1</a>",string)

    #Convert MathJax @@...@@ -> <span>@@...@@</span>
    #and $$...$$ -> <div>$$..$$</div> to protect
    #from Markdown formatter, also replace \_ -> _ in 
    #Latex string
    string = re.sub(r"(@@.+?@@)",partial(processMathJax,delimit="@@"),string)
    string = re.sub(r"(\$\$.+?\$\$)",partial(processMathJax,delimit="$$"),string,flags=re.DOTALL|re.MULTILINE)
    string = re.sub(r"(\\begin{align}.+?\\end{align})",partial(processMathJax,delimit="align"),string,flags=re.DOTALL|re.MULTILINE)

    string = re.sub(r"([ ]*)include:(\S+)",partial(includeFile),string)

    #Convert wiki links to markdown link syntax
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
                mdstring += "<a href='%s?page=%s'>%s</a>"%(this_fname,link,name)
            else:
                #Otherwise use the raw link name (file -> file.md)
                mdstring += "<a href='%s?page=%s'>%s</a>"%(this_fname,chunk,chunk)

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

    #
    # Markdown2 Renderer
    #
    #htmlstring = markdown2.markdown(mdstring)

    ##
    ## Standard Python Markdown Renderer
    ##
    #htmlstring = markdown.markdown(mdstring,
    #             extensions=["markdown.extensions.codehilite",
    #                         "markdown.extensions.fenced_code"],
    #                         #"markdown.extensions.nl2br"],
    #             extension_configs = 
    #             {
    #             "markdown.extensions.codehilite" :
    #                 {
    #                 "css_class" : "highlight"
    #                 }
    #             })

    ##
    ## Mistune Markdown Renderer
    ##
    renderer = MyRenderer()
    md = mistune.Markdown(renderer=renderer)
    htmlstring = md.render(mdstring)

    #Convert TeX \sub commands to underscores
    htmlstring = re.sub(r"\\sub",r"_",htmlstring)

    return htmlstring

page = form.getvalue("page")

if page == None: page = "main"

mdfname = reldocpath + page + ".md"
mdfile = openFile(mdfname)

# "page.md" file doesn't exist, reinterpret "page" as a
# directory name and look for a main.md file there
if not mdfile:
    mdfname = reldocpath + page + "/main.md"
    mdfile = openFile(mdfname)

printContentType()

bodyhtml = ""
if mdfile:
    bodyhtml = convert("".join(mdfile.readlines()))
    mdfile.close()
else:
    bodyhtml = "<p>(Documentation file not found)</p>"

# Generate directory tree hyperlinks
dirlist = page.split('/')
page_name = dirlist.pop(-1)

nav = ""

for dirname in dirlist:
    nav += "%s<a href=\"%s?page=%s\">%s</a>"%(nav_delimiter,this_fname,dirname,dirname)
if page_name != "main":
    nav += nav_delimiter+page_name
if not (len(dirlist) == 0 and page_name == "main"):
    nav = "<a href=\"%s?page=main\">main</a>%s</br>"%(this_fname,nav)


prenav_header_file = open(prenav_header_fname)
postnav_header_file = open(postnav_header_fname)
footer_file = open(footer_fname)
print "".join(prenav_header_file.readlines())
print nav
print "".join(postnav_header_file.readlines())
print bodyhtml

#
# Auto-generate back links
#
backlinks = []
full_dirname = ""
for dirname in dirlist:
    text = "Back to " + dirname.capitalize()
    full_dirname += dirname
    iconfname = "docs/"+full_dirname+"/icon.png"
    iconimg = "<!-- " + iconfname + " -->"
    if fileExists(iconfname): iconimg = "<img src=\"%s\" class=\"icon\">"%(iconfname,)
    backlinks.append( "<br/>%s<a href=\"%s?page=%s\">%s</a>"%(iconimg,this_fname,full_dirname,text) )
    full_dirname += "/"
backlinks.reverse()
for bl in backlinks: print bl

if not (len(dirlist)==0 and page_name == "main"):
    print "<br/><img src=\"docs/icon.png\" class=\"icon\"><a href=\"%s\">Back to Main</a>"%(this_fname)

print "".join(footer_file.readlines())
footer_file.close()
#header_file.close()
