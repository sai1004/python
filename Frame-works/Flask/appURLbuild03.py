from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route('/admin')
def hello_admin():
    return 'hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello {} as Guest '.format(guest)


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
