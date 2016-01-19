#!/usr/bin/env python

from __future__ import print_function

import sys, os, cgi

print("#soadopted!", file=sys.stderr)

print("Location: http://google.ca/")
print("Content-type: text/plain")
print("")
print("")
print("Hi I'm adopted")
print("I am process %i" % os.getpid())

print(os.environ)
print("")
form = cgi.FieldStorage()
print(form.getvalue('x'))
