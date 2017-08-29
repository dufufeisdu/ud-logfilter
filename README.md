#How to use
##step 1
  Set up the vagrant and postgreSQL
##step 2
  [download data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
	unzip into the vagrant
  In vagrant Load data: psql -d news -f newsdata.sql
##step 3
In terminal create these views:
* create view popularlog as select path,count(*) as viewed from log where status='200 OK' and path like '/article/%' group by path order by viewed desc;
* create view daily_request as select count(*) as num,to_char(log.time,'MM-DD-YYYY') as daily from log group by daily order by daily desc;
* create view daily_error as select count(*) as err_num, to_char(log.time,'MM-DD-YYYY') as daily from log where log.status like '4%' group by daily order by daily desc;
##step 4
	In vagrant, $ python3 relace_with_your_dir/file_name
	The output will be shown in terminal
