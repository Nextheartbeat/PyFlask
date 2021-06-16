# coding=utf -8
# TODO: 唯一URL
from flask import Flask

app = Flask(__name__)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)


"""

"""