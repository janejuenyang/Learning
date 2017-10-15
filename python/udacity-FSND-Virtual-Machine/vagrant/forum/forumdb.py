# "Database code" for the DB Forum.

import psycopg2
import bleach

def get_posts():
    """Return all posts from the 'database', most recent first."""
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute("SELECT time, content FROM posts ORDER BY time DESC")
    posts = ({'content': str(bleach.clean(str(row[1]))), 'time': str(row[0])}
        for row in c.fetchall())
    DB.close()
    return posts

def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    content = bleach.clean(content)
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    DB.commit()
    DB.close()


