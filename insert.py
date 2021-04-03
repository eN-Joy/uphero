# -*- coding: utf-8 -*-
import json
import psycopg2

conn = psycopg2.connect(dbname='uphero',
                        user='zhou3594',
                        host='localhost',
                        password='########')

cur = conn.cursor()

json_data = open('short.json')
data = json.load(json_data)

for article in data:
    try:
        title = article['title'][0]
    except KeyError:
        title = u'无标题'

    originator = article['poster'][0]
    pub_date = article['pdate']
    content = article['content']
    category_id = 4
    link = article['post_url'][0]
    media = json.dumps(article['urls'])
    # link = article['post_url']
    # media = article['urls']
    
# for article in data[:5]:
#     print '### Problem here ###'
#     print article['title']
#     print type(article['title']) # <type 'list'>
#     print type(article['title'][0]) # <type 'unicode'>
#     print article['poster']
#     print article['pdate']
#     print article['content']
#     print 1
#     print article['post_url']
#     print article['urls']

    query = """
    INSERT INTO ktv_article
    (title, originator, pub_date, content, category_id, link, media)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    record = (title, originator, pub_date, content, category_id, link, media)
    cur.execute(query, record)
    conn.commit()


















