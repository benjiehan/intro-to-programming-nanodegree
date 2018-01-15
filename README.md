# Logs Analysis Project

## Pre-requisites:
  * [Vagrant](https://www.vagrantup.com/)
  * [Python3](https://www.python.org/)
  * [Git BASH](https://git-for-windows.github.io/)
  * [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
  * [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Running the project:
  1. Install Vagrant & Python3.
  2. Place [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) into any folder on your local machine (I recommend your home directory for ease of navigation).
  3. Unzip [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), and place 'newsdata.sql' into the fullstack-nanodegree-vm/vagrant directory.
  4. The Python script, 'run_queries.py' should also be placed into the fullstack-nanodegree-vm/vagrant directory.
  
## Launching the VM:
  1. Launch Git Bash.
  2. Navigate to the fullstack-nanodegree-vm/vagrant directory - I placed my folder in the home directory and navigated with 'cd fullstack-nanodegree-vm/vagrant'.
  3. Launch the VM:
  
```
 $ vagrant up
```
  4. Log in with:
  
```
$ vagrant ssh
```
  3. Go to relevant directory `cd /vagrant` and `ls`. You should have a few files listed here, including 'newsdata.sql'.
  
## Downloading the data:
  1. Load the data in local database using the command:
  
```
psql -d news -f newsdata.sql
```
  * Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
    * `psql` — the PostgreSQL command line program
    * `-d news` — connect to the database named news which has been set up for you
    * `-f newsdata.sql` — run the SQL statements in the file `newsdata.sql'

## Creating the views: 
 Input 'psql -d news'. Your prompt should look like this 'news=>'. Copy and paste the paragraphs below one at a time:
 
``` 
create view top_3_articles as
select title, count(*) as page_views
from articles join log
on log.path = concat('/article/', articles.slug)
where status !='404 NOT FOUND'
group by articles.title
order by page_views desc;
```

```
create view top_authors as
select author, count(*) as page_views
from articles join log
on log.path = concat('/article/', articles.slug)
where status !='404 NOT FOUND'
group by articles.author 
order by page_views desc;
```

```
create view All_Requests2 as
select time ::timestamp::date as date, count(*) as total_requests
from log
group by date
order by total_requests desc;
```

```
create view All_Errors2 as
select time ::timestamp::date as date, count(*) as requests_failures
from log
where status = '404 NOT FOUND'
group by date
order by requests_failures desc;
```

```
create view daily_error_number2 as
select All_Errors2.date,
cast(All_Errors2.requests_failures as decimal) / cast(All_Requests2.total_requests as decimal) as daily_error
from All_Requests2 join All_Errors2
on All_Requests2.date = All_Errors2.date
order by daily_error desc;
```

```
create view daily_error_percentage_table as
select date,
round(100 * (daily_error), 2) as daily_error_percentage
from daily_error_number2
order by daily_error_percentage desc limit 5;
```

## Pulling the report
  * After the views have been created, press CTRL + Z to exit the database. Input 'python run_queries.py' to run the script.
  * The python file `run_queries.py` executes 3 functions, printing out the answers onto the terminal.
