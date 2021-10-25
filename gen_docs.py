#!/usr/local/opt/python/libexec/bin/python
# ! /usr/bin/env python

import sys
import re #regular expressions
from cgi import FieldStorage
import Cookie
import datetime
import os
#import markdown2
#import markdown

import mistune #Markdown renderer
from pygments import highlight
from pygments.lexers import CppLexer
from pygments.lexers import JuliaLexer
from pygments.formatters import HtmlFormatter

from functools import partial
# Turn on cgitb to get nice debugging output.
# Remember to turn off when done debugging, otherwise not secure.
#import cgitb; cgitb.enable()

#################################

# version name, display name, associated language
versions = [
            #["julia","Julia","Julia"],
            ["cppv3","C++","C++"], 
            #["cppv2","C++v2","C++"],
            ]
default_version = "cppv3"

reldocpath = "docs/"
prenav_header_fname = "docs_header_prenav.html"
postnav_header_fname = "docs_header_postnav.html"
footer_fname = "docs_footer.html"
this_fname = "docs.cgi"
nav_delimiter = "&nbsp;/&nbsp;"

#################################

sys.path.append("/opt/itensor.org/")

class MyRenderer(mistune.Renderer):
    mylang = "C++"
    def block_code(self, code, lang):
        lexer = CppLexer()
        if self.mylang == "C++":
            lexer = CppLexer()
        elif self.mylang == "Julia":
            lexer = JuliaLexer()

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

def printContentType(vers):
    print("Content-Type: text/html")
    #if vers != None:
    #expiration = datetime.datetime.now() + datetime.timedelta(days=30)
    #cookie = Cookie.SimpleCookie()
    #cookie["vers"] = vers
    #cookie["vers"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
    #print cookie.output()
    print "\n"

def processMathJax(matchobj,delimit=""):
    if delimit=="@@":
        math = re.sub(r"\\_","_",matchobj.group(0))
        return "<span> " + math + " </span> "
    elif delimit=="$$":
        white = matchobj.group(1)
        math = re.sub(r"\\_","_",matchobj.group(2))
        #return "\n{}<div>\n{}{}\n{}</div>\n<!-- -->".format(white,white,math,white)
        return "\n{}<div>\n{}{}\n{}</div>\n".format(white,white,math,white)
    elif delimit=="align":
        white = matchobj.group(1)
        math = re.sub(r"\\_","_",matchobj.group(2))
        #return "\n{}<div>\n{}{}\n{}</div>\n<!-- -->".format(white,white,math,white)
        return "\n{}<div>\n{}{}\n{}</div>\n".format(white,white,math,white)
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
    

def openMDFile(vdocpath,page):
    mdfname = vdocpath + page + ".md"
    mdfile = openFile(mdfname)

    # "page.md" file doesn't exist, reinterpret "page" as a
    # directory name and look for a main.md file there
    if not mdfile:
        mdfname = vdocpath + page + "/main.md"
        mdfile = openFile(mdfname)

    return mdfile

def convert(string,vers,lang):
    #Convert SciPost[Vol,Issue,PageNum]tags
    string = re.sub(r"SciPost\[(\d+),(\d+),(\d+)\]",r"<i style='color:#CC0000'>SciPost Phys.</i>&nbsp;&nbsp;<b>\1</b> <a href='https://scipost.org/10.21468/SciPostPhys.\1.\2.\3'>\3</a>",string)

    #Convert PhysRev[Letter,Vol,PageNum]tags
    string = re.sub(r"PhysRev\[(.+?),(\d+),(\d+)\]",r"<i style='color:#CC0000'>Phys.&nbsp;Rev.&nbsp;\1</i>&nbsp;&nbsp;<b>\2</b> <a href='https://doi.org/10.1103/PhysRev\1.\2.\3'>\3</a>",string)

    #Convert arxiv:####.#### links
    string = re.sub(r"arxiv:(\d\d\d\d\.\d+)",r"arxiv:<a target='_blank' href='http://arxiv.org/abs/\1'>\1</a>",string)

    #Convert cond-mat/####### links
    string = re.sub(r"cond-mat/(\d\d\d\d\d\d\d)",r"<a target='_blank' href='http://arxiv.org/abs/cond-mat/\1'>cond-mat/\1</a>",string)

    #Convert github:<sha> links
    string = re.sub(r"github:(\w{5})\w*",r"<a class='github' target='_blank' href='https://github.com/ITensor/ITensor/commit/\1'>\1</a>",string)

    #Convert #nn github issue and PR links
    if lang=="Julia":
        string = re.sub(r"(Request|request|Pull|pull|PR) #(\d+)",r"\1 <a target='_blank' href='https://github.com/ITensor/ITensors.jl/pull/\2'>#\2</a>",string)
        string = re.sub(r"(Issue|issue|Bug|bug) #(\d+)",r"\1 <a target='_blank' href='https://github.com/ITensor/ITensors.jl/issues/\2'>#\2</a>",string)
    else:
        string = re.sub(r"(Request|request|Pull|pull|PR) #(\d+)",r"\1 <a target='_blank' href='https://github.com/ITensor/ITensor/pull/\2'>#\2</a>",string)
        string = re.sub(r"(Issue|issue|Bug|bug) #(\d+)",r"\1 <a target='_blank' href='https://github.com/ITensor/ITensor/issues/\2'>#\2</a>",string)

    #Convert VERSION token
    string = re.sub(r"VERSION",vers,string)

    #Convert MathJax @@...@@ -> <span>@@...@@</span>
    #and $$...$$ -> <div>$$..$$</div> to protect
    #from Markdown formatter, also replace \_ -> _ in 
    #Latex string
    string = re.sub(r"(@@.+?@@)",partial(processMathJax,delimit="@@"),string)
    string = re.sub(r"([ ]*)(\$\$.+?\$\$)",partial(processMathJax,delimit="$$"),string,flags=re.DOTALL|re.MULTILINE)
    string = re.sub(r"([ ]*)(\\begin{align}.+?\\end{align})",partial(processMathJax,delimit="align"),string,flags=re.DOTALL|re.MULTILINE)

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
                mdstring += "<a href='%s?vers=%s&page=%s'>%s</a>"%(this_fname,vers,link,name)
            else:
                #Otherwise use the raw link name (file -> file.md)
                mdstring += "<a href='%s?vers=%s&page=%s'>%s</a>"%(this_fname,vers,chunk,chunk)

    ##
    ## Mistune Markdown Renderer
    ##
    renderer = MyRenderer()
    renderer.mylang = lang
    md = mistune.Markdown(renderer=renderer)
    htmlstring = md.render(mdstring)

    #Convert TeX \sub commands to underscores
    htmlstring = re.sub(r"\\sub",r"_",htmlstring)

    return htmlstring

def generate():
    page = form.getvalue("page")
    vers = "cppv3"
    #vers = form.getvalue("vers")
    lang = "C++"
    #for v in versions:
    #    if v[0]==vers: lang = v[2]

    #Cookie_val = ""
    #Try:
    #    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    #    cookie_val = cookie["vers"].value
    #Except (Cookie.CookieError, KeyError): 
    #    cookie_val = default_version

    #If vers == None: vers = cookie_val


    if page == None: page = "main"

    vdocpath = reldocpath + "/" + vers + "/"

    mdfile = openMDFile(vdocpath,page)

    # If file or folder not found in given
    # version, look in 'all' folder as a fallback
    inall = False
    if not mdfile:
        all_docpath = reldocpath + "/all/"
        inall = True
        mdfile = openMDFile(all_docpath,page)

    #
    # Start generating the page
    #
    printContentType(vers)

    bodyhtml = ""
    if mdfile:
        bodyhtml = convert("".join(mdfile.readlines()),vers,lang)
        mdfile.close()
    else:
        bodyhtml = "<p>Documentation for the Julia version, can be found <b><a href=\"https://itensor.github.io/ITensors.jl/stable/index.html\">at this link.</a></b></p>"

    # Generate directory tree hyperlinks
    dirlist = page.split('/')
    page_name = dirlist.pop(-1)

    # Create navigation line
    nav = ""
    for dirname in dirlist:
        nav += "%s<a href=\"%s?page=%s&vers=%s\">%s</a>"%(nav_delimiter,this_fname,dirname,vers,dirname)

    if page_name != "main":
        nav += nav_delimiter+page_name

    if not (len(dirlist) == 0 and page_name == "main"):
        nav = "<a href=\"%s?page=main&vers=%s\">main</a>%s"%(this_fname,vers,nav)

    nav = "<span style='float:left;'>" + nav + "</span>"

    ## Create version information line
    #vinfo = "<span class='versions' style='float:right;'>"
    #n = 0
    #lang = "C++"
    #for (v,vname,vlang) in versions:
    #    if n > 0: vinfo += "&nbsp;|&nbsp;"
    #    if v == vers:
    #        vinfo += "<span style='outline:solid 1px;font-weight:bold;'>%s</span>"%(vname)
    #        lang = vlang
    #    else:
    #        vinfo += "<a style='text-decoration:none;' href=\"%s?page=%s&vers=%s\">%s</a>"%(this_fname,page,v,vname)
    #    n += 1
    #vinfo += "</span></br>"

    #
    # Generate Back-Links
    #
    backlinks = []
    full_dirname = ""
    for dirname in dirlist:
        nice_dirname = re.sub(r"_",r" ",dirname).title()
        text = "Back to " + nice_dirname
        full_dirname += dirname
        iconfname = "docs/"+vers+"/"+full_dirname+"/icon.png"
        iconimg = "<!-- " + iconfname + " -->"
        if fileExists(iconfname): iconimg = "<img src=\"%s\" class=\"icon\">"%(iconfname,)
        backlinks.append( "<br/>%s<a href=\"%s?page=%s&vers=%s\">%s</a>"%(iconimg,this_fname,full_dirname,vers,text) )
        full_dirname += "/"
    backlinks.reverse()

    #
    # Special handling of "codes" docs file
    # to make top link for Codes be colored white
    #
    prenav_fname_to_use = prenav_header_fname
    if full_dirname+page_name == "codes":
        prenav_fname_to_use = "docs_header_codes_prenav.html"

    prenav_header_file = open(prenav_fname_to_use)
    postnav_header_file = open(postnav_header_fname)
    footer_file = open(footer_fname)
    print "".join(prenav_header_file.readlines())
    print nav
    #print vinfo
    print "".join(postnav_header_file.readlines())
    #if vers == "cppv3" and (not inall):
    #    print "<span style='color:red;'>ITensor version 3 has not been released yet. \
    #           This documentation is a preview only.</span><br/><br/>" 
    print bodyhtml

    for bl in backlinks: print bl

    if not (len(dirlist)==0 and page_name == "main"):
        print "<br/><img src=\"docs/%s/icon.png\" class=\"icon\"><a href=\"%s?vers=%s\">Back to Main</a>"%(vers,this_fname,vers)

    print "".join(footer_file.readlines())
    footer_file.close()
    #header_file.close()
