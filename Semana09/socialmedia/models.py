import sqlite3 as sql, os

ROOT = os.path.dirname(os.path.relpath((__file__)))

def create_post(name, content):
    con = sql.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    con.execute('select * from posts')
    posts = cur.fetchall()
    return posts