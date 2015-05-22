from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, decode_responses=True)


@app.route('/')
def hello():
    redis.incr('plunders')
    redis.decr('booty')
    return 'Yarrrr matey!  I have been plundered %s times.  %s booty remains.' % (redis.get('plunders'), redis.get('booty'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
