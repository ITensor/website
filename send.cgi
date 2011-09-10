#!/usr/bin/python

docpath = "/var/www/html/itensor/docs/"

from markdown2 import Markdown
markdowner = Markdown()

#import cgitb
#cgitb.enable()

import cgi
form = cgi.FieldStorage()

md = form["value"].value

mdfile = open(docpath + "main.md",'w')
mdfile.write(md)
mdfile.close()

html = markdowner.convert(md)
htmlfile = open(docpath + "main_body.html",'w')
htmlfile.write(html)
htmlfile.close()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print html
