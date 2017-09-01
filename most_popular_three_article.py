#!/usr/bin/env python3
import psycopg2
DBNAME = "news"


def most_popular_three_aritcles():
    """Return the most popular three articles in news database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select articles.title, popularlog.viewed
              from articles, popularlog
              where substring(popularlog.path from 10)=articles.slug
              limit 3
              """)
    column_names = tuple([desc[0] for desc in c.description])
    articles = c.fetchall()
    articles.insert(0, column_names)
    db.close()
    for title, views in articles:
        print('{0:<42}{1:<42}'.format(title, views))


if __name__ == '__main__':
    most_popular_three_aritcles()
