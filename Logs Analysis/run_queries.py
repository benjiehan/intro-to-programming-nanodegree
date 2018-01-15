#!/usr/bin/env python3

import psycopg2
from datetime import datetime


def connect(query):
    """
    function connects to the database to fetch results
    """
    try:
        database = psycopg2.connect(database="news")
        c = database.cursor()
        c.execute(query)
        query_results = c.fetchall()
        database.close()
        return query_results
    except BaseException:
        print('Failed to fetch results from database')


def print_results(query_results):
    """
    function prints results
    """
    for i in query_results:
        print('"' + i[0] + '"' + ' -- ' + i[1])
    print '\n'

# IMPORTANT: Refer to the README to create views before running!

# Q1 - Three most popular articles of all time


def popular_articles():
    print ' Top Three Articles '
    print '--'
    query1 = """
            select title, concat(concat(page_views,' '), 'views')as views
            from top_3_articles limit 3;
            """
    articles = connect(query1)
    print_results(articles)

# Q2- Most popular article authors of all time


def popular_authors():
    print ' Most Popular Authors '
    print '--'
    query2 = """
            select name, concat(concat(page_views,' '), 'views')as views
            from top_authors join authors on top_authors.author = authors.id
            limit 4;
            """
    authors = connect(query2)
    print_results(authors)

# Q3 - Days that more than 1% of requests led to errors


def error_days():
    print ' Days Where Error > 1% '
    print '--'
    query3 = """
            select date, concat(concat(daily_error_percentage,'%'), ' errors')
            as percentage
            from daily_error_percentage_table limit 1;
            """
    error_request = connect(query3)
    for i in error_request:
        print(i[0].strftime('%B %d, %Y') + ' -- ' + i[1])
    print '\n'


if __name__ == "__main__":
    popular_articles()
    popular_authors()
    error_days()
