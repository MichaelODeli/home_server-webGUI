#!/bin/python3
#!C:/Users/danie/AppData/Local/Programs/Python/Python38/python.exe
import HTML
import fileSearch
# import fileManager
import cgi, cgitb
cgitb.enable()
# cgi.enable()   #not sure if I need both 
# import logging
import traceback
import datetime
import configparser
cfg = configparser.ConfigParser()
with open('settings.ini', 'r', encoding='utf-8') as fp:
    cfg.read_file(fp)
# logging.basicConfig(format = u'%(levelname)-s [%(asctime)s] %(message)s', level = logging.WARN, filename = u'search-access.log')
try:
    form = cgi.FieldStorage()
    text1 = form.getfirst("filename", "None")
    if form.getvalue('device'):
        device = form.getvalue('device')
    else:
        device = 'pc'
    # text1 = 'alex'
    # device = 'PC'
    results = fileSearch.search(type='all', filename=text1)
    res = []
    now = datetime.datetime.now()
    created = now.strftime(r'%d/%m/%Y %H:%M:%S')
    try:
        resu = int(len(results))
        res = [None] * resu
        # res = np.empty(resu)
        r = 0
        # link_template = '<a target="_blank" href="{url}">{filename}</a>'
        link_template = '<a href="{url}">{filename}</a>'
        for result in results:
            waying = result[0]+'/'+result[2]+'/'+result[3]
            contentlist = ['films', 'serials', 'youtube']
            # urlf = cfg.get('links', 'webdir')+cfg.get('settings', 'storageFolder')+'/'+waying
            if device == 'mobile' and result[0] in contentlist:
                urlf = 'vlc://'+cfg.get('links', 'webdir')+cfg.get('settings', 'storageFolder')+'/'+waying
                urlf = urlf.replace('http://', '')
            # elif device == 'pc' and result[0] in contentlist:
            #     urlf = 'runapp:vlc '+cfg.get('links', 'webdir')+cfg.get('settings', 'storageFolder')+'/'+waying
            #     urlf = urlf.replace('http://', '')
            else:
                urlf = cfg.get('links', 'webdir')+cfg.get('settings', 'storageFolder')+'/'+waying
            filenamef = result[3]
            link = link_template.format(url=urlf, filename=filenamef)
            result.append(link)
            res[r] = result
            r+=1
        htmlcode = HTML.table(results)
    except IndexError:
        if str(results[0][0]) == 'Not found':
            htmlcode = str(results[0][0])
        else:
            htmlcode = 'Error. Report to system administrator with this timestamp '+created
            # logging.error(traceback.format_exc())
    print("Content-type: text/html")
    print('')
    print("<center><h1>Search results</h1>")
    print(htmlcode)
    print('<p></p>')
    print('<input type="button" onclick="history.back();" value="Назад"/></center>')
except Exception as e:
    print("Content-type: text/html")
    print('')
    print(traceback.format_exc())
    # logging.warn(e)
    # print('Error. Report to system administrator with this timestamp '+created)
