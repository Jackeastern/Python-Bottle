# pip install bottle
# https://bottlepy.org/docs/dev/tutorial.html
from bottle import route, run, template, request
import sqlite3


@route('/')
@route("/<home>")
def home(name="home"):
    return template('home', name=name)


@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


run(host='localhost', port=8080, debug=True, reloader=True)
