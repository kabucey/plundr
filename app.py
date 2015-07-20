from flask import Flask, json
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, decode_responses=True)


@app.route('/')
def home():
    plunder()
    return 'Yarrrr matey!  I have been plundered %s times.  %s booty remains.' % (redis.get('plunders'), redis.get('booty'))

@app.route('/api/plunder')
def api_plunder():
    """Plunders the booty and returns a json status."""
    plunder()
    dict = {
        "plunders": int(redis.get('plunders')),
        "booty": int(redis.get('booty'))
    }
    return json.jsonify(dict)

def plunder():
    redis.incr('plunders')
    redis.decr('booty')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
