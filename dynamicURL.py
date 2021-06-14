# coding=utf -8
from flask import Flask

app = Flask(__name__)


@app.route('/item/<id>/')
def item(id):
    return 'Item:{}'.format(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

"""
    尖括号中的内容是动态的,凡是匹配到/item/前缀的URL都会被映射到这个路由上, 在内部把id作为参数而获得
    它使用了特殊的字段标记<variable_name>，默认类型是字符串。
    如 果需要指定参数类型需要标记成<converter:variable_name>这样的格式， converter有下面几种。
        string:接受任何没有斜杠“/”的文本(默认)。 
        int:接受整数。 
        float:同int，
        但是接受浮点数。 
        path:和默认的相似，但也接受斜杠。 
        uuid:只接受uuid字符串。 
        any:可以指定多种路径，
        但是需要传入参数。
"""