#!/usr/bin/env python3
import psycopg2
DBNAME = "news"


def most_popular_author():
    """Return the most popular author and their reviwed aritcles"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select authors.name, sum(popularlog.viewed) as views
              from popularlog, authors, articles
              where authors.id=articles.author
              and substring(popularlog.path from 10)=articles.slug
              group by authors.name
              order by views desc
              """)
    column_names = tuple([desc[0] for desc in c.description])
    articles = c.fetchall()
    articles.insert(0, column_names)
    db.close()
    for author, views in articles:
        print('{0:<42}{1:<42}'.format(author, views))
    return articles


if __name__ == '__main__':
    most_popular_author()
