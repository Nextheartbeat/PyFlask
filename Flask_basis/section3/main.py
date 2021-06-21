# TODO: 请求
from flask import Flask, request

app = Flask(__name__)


# 请求的基础数据
@app.route('/base_info', methods=['get', 'post'])
def base_info():
    print(f'url: {request.url}')  # 请求的URL
    print(f'method: {request.method}')  # 本次请求的请求方式
    print(f'headers: {request.headers}')  # 获取请求头信息  类字典对象

    print(f'header-host: {request.headers["Host"]}')
    print(f'header-host: {request.headers.get("Host")}')  # 建议使用get方法, 键不存在不报错

    return 'base_info'


# 获取查询字符串, 表单
@app.route('/args_form', methods=['get', 'post'])
def args_form():
    # 获取查询字符串 -> request.args xx?name=zs&age=20 类字典对象
    print(request.args)
    print(request.args.get('a'))
    print(request.args.get('b'))
    # 获取参数所有值
    print(request.args.getlist('b'))

    # 获取post键值对 -> request.form 类字典对象
    print(request.form)
    print(request.form.get('form-a'))
    # 获取参数所有值
    print(request.form.getlist('form-a'))

    return 'args_form'


# 获取请求体数据原始字节流, json 请求字典
@app.route('/data_json', methods=['get', 'post'])
def data_json():
    # request.data 获取请求体数据原始字节数据
    print(request.data)
    print(request.json)

    return 'data_json'


# 上传的文件
@app.route('/files', methods=['get', 'post'])
def files():
    # request.files 获取用户上传的文件, 类字典对象
    print(request.files)
    file1 = request.files.get("upload_file_1")  # type : FileStorage
    print(type(file1))
    # 将文件保存到本地
    file1.save('test.png')

    # 获取图片的二进制数据
    file2 = request.files.get("upload_file_2")
    img_bytes = file2.read()
    print(img_bytes)

    return "files"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)

"""
flask的请求数据通过 request 对象来获取
常用属性：
属性	    说明	                        类型
url	    记录请求的URL地址	            str
method	记录请求使用的HTTP方法	        str
headers	记录请求中的报文头	            EnvironHeaders 类字典对象
args	记录请求中的查询参数	        MultiDict
form	记录请求中的表单数据	        MultiDict
data	记录请求的数据，并转换为字符串	bytes
json	记录请求体中的json数据	        Dict
files	记录请求上传的文件	            MultiDict[str: FileStorage]

"""

# TODO:
# 基础信息 url、method、headers

# 查询字符串 args、表单 form

# data 和 json

# 文件 files 类似于字典 value 是 FileStorage 文件对象，注意:要用 POST 或者其他方法来上传文件
#    可以通过 save 方法来保存到本地
#    可以用 read 方法来读取文件的字节码数据
#    注意:
#        - 如果调用 FileStorage 文件对象的 save 之后，就不能再继续调用 read 了，因为数据已经在 save 调用时读取完了
#        - 同样如果调用了 read 之后也不能再掉用了 save 了，因为 read 会把数据全部读取完
