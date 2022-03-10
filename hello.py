from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort


app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    body = '<h1>Hello World!</h1><p>Your browser is {}</p>'.format(user_agent)
    response = make_response(body)
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    if name == "joe":
        return redirect("http://www.iadt.ie")
    
    if name == "jim":
        abort(404)
        
    return '<h1>Hello, {}!</h1>'.format(name)