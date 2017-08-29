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
    for row in articles:
        print('%-42s%-42s' % (row[0], row[1]))
    return articles


most_popular_author()
