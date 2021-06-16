# coding=utf -8
# TODO: HTTP方法
from flask import Flask

app = Flask(__name__)

'''
@app.route('/login', methods=['GET', 'POST'])
@app.route('/j/item/<id>', methods=['DELETE', 'POST'])
'''


"""
GET:获取资源，GET操作应该是幂等的。 
HEAD:想要获取信息，但是只关心消息头。应用应该像处理GET 请求一样来处理它，但是不返回实际内容。 
POST:创建一个新的资源。 PUT:完整地替换资源或者创建资源。PUT操作虽然有副作用，但 应该是幂等的。 
DELETE:删除资源。DELETE操作有副作用，但也是幂等的。 
OPTIONS:获取资源支持的所有HTTP方法。

PATCH:局部更新，修改某个已有的资源
"""