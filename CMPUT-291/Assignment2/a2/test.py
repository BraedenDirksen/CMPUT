

import sqlite3,sys

db_path = sys.argv[1]

connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor.execute(" PRAGMA foreign_keys=ON; ")
connection.commit()

keywords = ['what','i']
query_1 = '''
select *
from posts
'''

query_2 = """
select *
from ?
where posts.title like '%?%'
or posts.body like '%?%'
or posts.pid in (select pid from tags where tags.tag like '%?%')
"""

cursor.execute(query_2, (cursor.execute(query_1),keywords[0],keywords[0],keywords[0]))


#something to change cursor to the table of last???
for keyword in keywords:
    cursor.execute(query, (keyword,keyword,keyword))
