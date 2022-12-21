# pip install bottle
# https://bottlepy.org/docs/dev/tutorial.html
from bottle import route, run, template


@route('/')
@route("/<home>")
def home(name="home"):
    return template('home', name=name)


run(host='localhost', port=8080, debug=True, reloader=True)
