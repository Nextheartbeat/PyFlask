# TODO: 响应 -重定向
from flask import Flask, jsonify, redirect

app = Flask(__name__)


@app.route('/response_json')
def response_json():
    data = {
        "name": "NextHeartbeat",
        "age": 18
    }
    return data


@app.route('/redirect')
def response_redirect():
    # redirect 中指定重定向的路径就可以
    return redirect('/response_json')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
    flask中通过 redirect() 实现重定向功能
"""