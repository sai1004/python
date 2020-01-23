from flask import Flask

app = Flask(__name__)

# app.route(rule, options)
# app.route('/', methods='POST')


@app.route('/')  # This goes to welcome page defaultly
def index():
    return 'We Are in welcome page.'


@app.route('/profile')
def profile():
    return ' We Are in Profile page.'


@app.route('/flask')
def hello_flask():
    return 'Hello Flask'


@app.route('/python/')
def hello_python():
    return 'Hello Python'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
