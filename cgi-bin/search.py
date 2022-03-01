#!C:/Users/danie/AppData/Local/Programs/Python/Python38/python.exe
import HTML
import fileSearch
import fileManager
import cgi
form = cgi.FieldStorage()
text1 = form.getfirst("filename", "None")
# text1 = 'free'
results = fileSearch.search(type='filename', filename=text1)
res = []
for result in results:
    link = '<a href="'+fileManager.getLinkId(id=result[1])+'">'+result[3]+'</a>'
    result.append(link)
    res.append(result)
htmlcode = HTML.table(results)
print("Content-type: text/html")
print()
print("<h1>Search results</h1>")
print(htmlcode)
print(' ')
print('<input type="button" onclick="history.back();" value="Назад"/>')
