#!/usr/bin/python3
print("Content-Type: text/html")
print()
import cgi , os

files = os.listdir('data')
listStr = ''

for item in files:
    listStr += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name = item)

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form['id'].value
    description = open('data/'+pageId,'r').read()
else:
    pageId = 'Welcome'
    description = 'Welcome Hello Web'

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <p><a href="create.py">Create</a></p>
  <form action="process_create.py">
  <p><input type="text" name="title" placeholder="title"></p>
  <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
  <p><input type="submit"></p>
  </form>

</body>
</html>
'''.format(title=pageId,desc=description, listStr = listStr))