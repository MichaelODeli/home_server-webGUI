#!C:/Users/danie/AppData/Local/Programs/Python/Python38/python.exe
import HTML
import fileSearch
import fileManager
import cgi
import logging
import traceback
import datetime
logging.basicConfig(format = u'%(levelname)-s [%(asctime)s] %(message)s', level = logging.WARN, filename = u'search-access.log')
try:
    form = cgi.FieldStorage()
    text1 = form.getfirst("filename", "None")
    results = fileSearch.search(type='filename', filename=text1)
    res = []
    now = datetime.datetime.now()
    created = now.strftime(r'%d/%m/%Y %H:%M:%S')
    try:
        resu = int(len(results))
        res = [None] * resu
        # res = np.empty(resu)
        r = 0
        for result in results:
            link = '<a target="_blank" href="'+fileManager.getLinkId(id=result[1])+'">'+result[3]+'</a>'
            # result.append(link)
            # res.append(result)
            result.append(link)
            res[r] = result
            r+=1
        htmlcode = HTML.table(results)
    except IndexError:
        if str(results[0][0]) == 'Not found':
            htmlcode = str(results[0][0])
        else:
            htmlcode = 'Error. Report to system administrator with this timestamp '+created
            logging.error(traceback.format_exc())
    print("Content-type: text/html")
    print()
    print("<center><h1>Search results</h1>")
    print(htmlcode)
    print('<p></p>')
    print('<input type="button" onclick="history.back();" value="Назад"/></center>')
except Exception as e:
    logging.fatal(traceback.format_exc())
    logging.warn(e)
    print('Error. Report to system administrator with this timestamp '+created)