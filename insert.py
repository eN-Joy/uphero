import json
import psycopg2


try:
    conn = psycopg2.connect("dbname='uphero' user='zhou3594' host='localhost' password='mary7718'")
except:
    print "I am unable to connect"

if conn:
    cursor = conn.cursor()
    
json_data = open('short.json')
data = json.load(json_data)


for article in data:
    # title = article['article']
    title = article['article'][0]
    originator = article['poster']
    pub_date = article['pdate']
    content = article['content']
    category_id = 1
    link = 'link url'
    media = 'link url'
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

    query = """INSERT INTO ktv_article (title, originator, pub_date,
    content, category_id, link, media) VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    record = (title, originator, pub_date, content, category_id, link, media)
    cursor.execute(query, record)
    # conn.commit()
    conn.close()







