#!/usr/bin/env python3
import psycopg2
DBNAME = "news"
ERROR_PERCENT = "'1'"


def certain_error_req_day():
    """Return date and request error that big than certain error percent"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select * from(select daily_error.daily as date,
						round(100*daily_error.err_num::numeric/daily_request.num,2)::text||'%'
						as error_rate
						from daily_error,daily_request
						where daily_error.daily=daily_request.daily) as foo
						where error_rate>{}""".format(ERROR_PERCENT))
    column_names = tuple([desc[0] for desc in c.description])
    articles = c.fetchall()
    articles.insert(0, column_names)
    db.close()
    for date, ratio in articles:
        print('{0:<42}{1:<42}'.format(date, ratio))
    return articles


if __name__ == '__main__':
    certain_error_req_day()
