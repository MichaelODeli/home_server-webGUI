#!/bin/python3
#!C:/Users/MichaelODeli/AppData/Local/Programs/Python/Python38/python.exe

from templates import html_templates
import cgi, cgitb
import traceback
try:
    cgitb.enable()
    form = cgi.FieldStorage()
    print("Content-type: text/html")
    print('')
    print(html_templates.title_header('Home server', header_active='home'))
    print('Somethingg')
except Exception as e:
    print("Content-type: text/html")
    print('')
    print(traceback.format_exc())
