from flask import Flask
from flask import abort

# from Incrementer.mem_incrementer import MemIncrementer
from Incrementer.redis_incrementer import RedisIncrementer

app = Flask(__name__)

# mem_incrementer = MemIncrementer()
mem_incrementer = RedisIncrementer()


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/increment', methods=['GET'])
def get_global_increment():
    result = mem_incrementer.get_global_increment()
    if result:
        return result
    abort(404)


@app.route('/increment/<session_id>', methods=['GET'])
def get_increment(session_id):
    result = mem_incrementer.get_increment(session_id)
    if result:
        return result
    abort(404)


@app.route('/increment/temp/<session_id>', methods=['GET'])
def get_increment_temp(session_id):
    result = mem_incrementer.get_increment_temp(session_id)
    if result:
        return result
    abort(404)

# GET /increment -> get global increment
# GET /increment/xyz -> get increment for session xyz
# GET /increment/temp/xyz -> get increment for session xyz


if __name__ == '__main__':
    app.run()
