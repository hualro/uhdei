#!/bin/python
from pymongo import Connection 

host= 'linus.mongohq.com' 
port = 10092 
dbName = 'uhdei' 
 
connection = Connection(host, port) 
db = connection[dbName] 
 
userID = 'uhdei' 
pwd = 'uhdei.301' 
db = connection[dbName]
db.authenticate(userID, pwd)

for collection in db.collection_names(): 
    print collection

