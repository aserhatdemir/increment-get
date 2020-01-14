from flask import Flask, request
from flask import abort

from Incrementer.mem_incrementer import MemIncrementer
# from Incrementer.redis_incrementer import RedisIncrementer

app = Flask(__name__)

incrementer = MemIncrementer()
# incrementer = RedisIncrementer()


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/increment', methods=['GET'])
def get_global_increment():
    result = incrementer.get_increment('global')
    if result:
        return result
    abort(404)


@app.route('/increment/<session_id>', methods=['GET'])
def get_increment(session_id):
    result = incrementer.get_increment(session_id)
    if result:
        return result
    abort(404)


@app.route('/increment/temp/<session_id>', methods=['GET'])
def get_increment_temp(session_id):
    result = incrementer.get_increment_temp(session_id)
    if result:
        return result
    abort(404)


@app.route('/increment/', methods=['GET'])
def get_value():
    search_key = request.args.get('q')
    result = incrementer.get_value(search_key)
    if result:
        return result
    abort(404)


@app.route('/increment/<session_id>', methods=['POST'])
def set_value(session_id):
    val = int(request.data)
    result = incrementer.set_value(session_id, val)
    if result:
        return result
    abort(404)


# GET /increment -> get global increment
# GET /increment/xyz -> get increment for session xyz
# GET /increment/temp/xyz -> get increment for session xyz
# GET /increment/?q=xyz -> get the value for xyz session
# POST /increment/xyz  -> write to value, value is given in body


if __name__ == '__main__':
    app.run()
