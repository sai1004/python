from flask import Flask

app = Flask(__name__)

# app.route(rule, options)
# app.route('/', methods='POST')


@app.route('/')  # This goes to welcome page defaultly
def index():
    return 'We Are in welcome page.'


#  passing variable in url
#  url will bw like http://0.0.0.0:8000/profile/bob

@app.route('/profile/<name>')
def profile(name):
    return ' Hello {}'.format(name)


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number {}'.format(postID)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
