"""FlaskによるDB用REST_APIサーバ
"""
import os
import re
import redis
from flask import (
    Flask,
    jsonify,
    request,
)

# Redis db conf
REDIS_HOST: str = os.environ['REDIS_HOST']
REDIS_PORT: int = int(os.environ['REDIS_PORT'])
REDIS_DB: int = int(os.environ['REDIS_DB'])

print('---- Check db access setting ----')
print('REDIS_HOST', REDIS_HOST)
print('REDIS_PORT', REDIS_PORT)
print('REDIS_DB', REDIS_DB)

print('Connect redis db server')
REDIS = redis.Redis(host=REDIS_HOST, 
                    port=REDIS_PORT,
                    db=REDIS_DB,
                    )
print('Redis db server: ', REDIS)

# App port (for this REST_API server)
APP_PORT = int(os.environ['APP_PORT'])

# REST_API server
app = Flask("rest-api app server")

API_VER = 'v1'
DB_STORE_COUNT = 1000000 # 100万

@app.route(f'/api/{API_VER}/keys/', methods=['GET'])
def api_keys():
    data = {}
    cursor = '0'
    while cursor != 0:
        cursor, keys = REDIS.scan(cursor=cursor,
                                  count=DB_STORE_COUNT,
                                  )
        if len(keys) == 0:
            break
        keys = [key.decode() for key in keys]
        values = [value.decode() for value in REDIS.mget(*keys)]
        data.update(dict(zip(keys, values)))
    
    return success(data)

@app.route(f'/api/{API_VER}/keys/<key>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_key(key):
    if not isalnum(key):
        print('key is not isalnum')
        return error(400.1)
    
    body = request.get_data().decode().strip()
    if request.method in ['POST', 'PUT']:
        if body == '':
            print('body empty')
            return error(400.2)
        if not isalnum(body):
            print('body is not alnum')
            return error(400.3)
    
    def get():
        value = REDIS.get(key)
        if value is not None: # valueが空
            return success({key:value.decode()})
        return error(404)
    
    def post():
        if REDIS.get(key) is not None: # 既にkeyが存在
            return error(409)
        REDIS.set(key, body)
        return success({key:body})
    
    def put():
        REDIS.set(key, body)
        return success({key:body})
    
    def delete():
        if REDIS.delete(key) == 0: # keyが空
            return error(404)
        return success({})
    
    func_dict = {
        'GET': get,
        'POST': post,
        'PUT': put,
        'DELETE': delete,
    }
    return func_dict[request.method]() # HTTPのAPIに応じてRedisとの仲介を行う

def isalnum(text):
    # 半角英数字で構成された文字列にマッチした場合, Trueを返す
    return re.match(r'^[a-zA-Z0-9]+$', text) is not None
    
def success(kv):
    # ブラウザにJson形式で値を返す
    return jsonify(kv), 200 # HTTPレスポンスコード 200 : 成功

def error(code):
    message = {
        400.1: "bad request. key must be alnum",
        400.2: "bad request. post/put needs value on body",
        400.3: "bad request. value must be alnum",
        404: "request not found",
        409: "resource conflict. resource already exist",
    }
    return jsonify({'error': message[code], 'code': int(code)}), int(code)

# 404 レスポンスコード(アクセスデータが存在しない) ハンドラ
@app.errorhandler(404)
def api_not_found_error(error):
    return jsonify({'error': "api not found", 'code': 404}), 404

# 405 レスポンスコード(アクセス権限) ハンドラ
@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({'error': "method not allowed", 'code': 405}), 405

# 500 レスポンスコード(サーバー内部エラー) ハンドラ
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'server internal error', 'code': 500}), 500


if __name__ == "__main__":
    """ Test connection for redis db server """
    # def get(key):
    #     value = REDIS.get(key)
    #     if value is None:
    #         raise Exception('key does not exist')
    #     return value.decode()

    # def post(key, value):
    #     if REDIS.get(key) is not None:
    #         raise Exception('key already exists')
    #     REDIS.set(key, value)

    # def put(key, value):
    #     REDIS.set(key, value)

    # def delete(key):
    #     if REDIS.get(key) is None:
    #         raise Exception('key does not exist')
    #     REDIS.delete(key)

    # print('[TEST]---> access redis db')
    # post('apple', 'red')
    # post('banana', 'yellow')
    # value = get('apple')
    # print(value) # => red
    # put('apple', 'green')
    # delete('banana')
    # print('[TEST]<---- access redis db')

    print('[Start] flask app server')
    app.run(debug=True,
            host='0.0.0.0',
            port=APP_PORT,
            )
