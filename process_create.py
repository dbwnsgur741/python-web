#!/usr/bin/python3
print("Content-Type: text/html")
print()

import sys # 모듈 임시경로 등록
import codecs # 한글처리
import cgi

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # 한글처리 2

form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

opened_file = open('data/'+title,'w',encoding='utf-8')
opened_file.write(description)
opened_file.close()

print("Location: index.py?id="+title)
print()