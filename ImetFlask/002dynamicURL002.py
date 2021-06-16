# coding=utf -8
# TODO: 动态URL规则
from flask import Flask

app = Flask(__name__)


@app.route('/<any(a,b):page_name>/')
def item(page_name):
    return 'page_name:{}'.format(page_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

"""
    访问/a/和访问/b/都符合这个规则，/a/对应的page_name就是a
"""