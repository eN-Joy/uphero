# -*- coding: utf-8 -*-
import os
import json
import psycopg2
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uphero.settings")
from ktv.models import Article

# conn = psycopg2.connect(dbname='uphero',
#                         user='zhou3594',
#                         host='localhost',
#                         password='^^^^^^^^')

# cur = conn.cursor()

json_data = open('short.json')
data = json.load(json_data)

for article in data[:100]:
    try:
        title = article['title'][0]
    except KeyError:
        title = u'无标题'

    try:
        originator = article['poster'][0]
    except KeyError:
        originator = u'无作者'

    pub_date = article['pdate']
    content = article['content']
    category_id = 4
    link = article['post_url'][0]
    media = json.dumps(article['urls'])

    p = Article(
        title=title,
        originator=originator,
        pub_date=pub_date,
        content=content,
        category_id=2,
        link=link,
        media=media,
        is_published=True,
        )

    p.save()
    p.tags.add(u'中文', u'英文', u'老歌', u'粤语', u'想唱就唱')
