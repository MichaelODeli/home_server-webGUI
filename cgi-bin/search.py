#!/bin/python3
#!C:/Users/MichaelODeli/AppData/Local/Programs/Python/Python38/python.exe
import HTML
import fileSearch
import cgi, cgitb
cgitb.enable()
# import logging
import traceback
import datetime
import configparser
import sys
if sys.platform == "linux" or sys.platform == "linux2":
    sys.path.append(r"/home/michael/server-side")
elif sys.platform == "win32":
    sys.path.append(r"C:\Users\MichaelODeli\OneDrive\DEVELOP\work\home-server\server-side")
from templates import html_templates
cfg = configparser.ConfigParser()
with open('settings.ini', 'r', encoding='utf-8') as fp:
    cfg.read_file(fp)
# logging.basicConfig(format = u'%(levelname)-s [%(asctime)s] %(message)s', level = logging.WARN, filename = u'search-access.log')
try:
    form = cgi.FieldStorage()
    text1 = form.getfirst("filename", "somethingshit")
    if form.getvalue('device'):
        device = form.getvalue('device')
    else:
        device = 'pc'
    if form.getvalue('searchtype'):
        searchTyping = form.getvalue('searchtype')
    else:
        searchTyping = 'all'
    if form.getvalue('fromvideo')=='True':
        from_video=True
    else: from_video=''
    results = fileSearch.search(searchType=searchTyping, filename=text1)
    res = []
    now = datetime.datetime.now()
    created = now.strftime(r'%d/%m/%Y %H:%M:%S')
    try:
        link_template = '<a href="{url}">{filename}</a>'
        for result in results:
            waying = result[0]+'/'+result[2]+'/'+result[3]
            contentlist = ['films', 'serials', 'youtube']
            if device == 'mobile' and result[0] in contentlist:
                urlf = ('vlc://'+cfg.get('links', 'webdir')+cfg.get('settings', 'storageFolder')+'/'+waying).replace('http://', '')
                res.append(urlf.replace('vlc://', 'http://'))
            else:
                if from_video!=True:
                    urlf = cfg.get('links', 'webdir')+cfg.get('settings', 'storageFolder')+'/'+waying
                else:
                    if '.mp4' in waying:
                        urlf = cfg.get('links', 'webdir')+'videoview.py?videoid={idd}'.format(idd=result[1])
                    else:
                        urlf = cfg.get('links', 'webdir')+cfg.get('settings', 'storageFolder')+'/'+waying
                if result[0] in contentlist: res.append(urlf)
            if len(result[3])>60:
                filenameLink=result[3].replace('-', ' ')[:60]+'...'
            else:
                filenameLink=result[3].replace('-', ' ')
            link = link_template.format(url=urlf, filename=filenameLink)
            result.append(link)
            del result[3]
        headTable = ['Type', 'ID', 'Category', 'Filename']
        htmlcode = HTML.table(results, header_row=headTable)
    except IndexError:
        if str(results[0][0]) == 'Not found':
            htmlcode = str(results[0][0])
        else:
            htmlcode = 'Error. Report to system administrator with this timestamp '+created
            # logging.error(traceback.format_exc())
    print("Content-type: text/html")
    print('')
    if device == 'mobile':
        print(html_templates.title_header('Home server - Search', search_text=text1, selectedmobile=True))
    else:
        if from_video==True:
            print(html_templates.title_header('Home server - Search', search_text=text1, from_video=True))
        else: 
            print(html_templates.title_header('Home server - Search', search_text=text1))
    print('''
    <body>
    <center><h1>Search results</h1>
    '''
    )
    print(htmlcode)
    print('<p></p>')
    print('</center></body></html>')

except Exception as e:
    print("Content-type: text/html")
    print('')
    print(traceback.format_exc())
    print(searchTyping)
    # logging.warn(e)
    # print('Error. Report to system administrator with this timestamp '+created)
