# UD Logfilter
>UD-Logfilter is a filter for database log. It uses psycopg2 to query a mock PostgreSQL database for a fictional news website.
## How to use
### step 1
  Set up the vagrant, use the Vagrantfile provided
### step 2
  [Download data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
	and unzip into the vagrant dir</br>
  In vagrant terminal, load data by : `psql -d news -f newsdata.sql`
### step 3
In vagrant terminal, pupular views by using this command:
`psql -d news -f create_views.sql`
### step 4
	In vargant termianl:
>1. To display the three most viewed articles in the news database, run: `python3 most_popular_three_article.py`
>2. To display the most popular article authors of all time, run:`pyhton3 most_popular_author.py`
>3. To display on which days did more than 1% of requests lead to errors run: `python3 error_ratio.py`
