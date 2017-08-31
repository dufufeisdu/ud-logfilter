# UD Logfilter
>UD-Logfilter is a filter for database log. It uses psycopg2 to query a mock PostgreSQL database for a fictional news website. It will return:
>* What are the most popular three articles of all time if you run
most_popular_three_article.py
>*  Who are the most popular article authors of all time if you run
most_popular_author.py
>* On which days did more than 1% of requests lead to errors if you
run error_ratio.py
## How to use
### step 1
  Set up the vagrant, use the Vagrantfile provided
### step 2
  [Download data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
	and unzip into the vagrant</br>
  In vagrant Load data: `psql -d news -f newsdata.sql`
### step 3
In terminal pupular views by using this command:
`psql -d news -f create_views.sql`
### step 4
	In vagrant, $ python3 relace_with_your_dir/file_name
	The output will be shown in terminal
