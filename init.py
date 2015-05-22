import os
from redis import Redis

redis = Redis(host='redis', port=6379, decode_responses=True)


def initialize_booty(amount):
    redis.set('booty', amount)


def main():
    booty = os.environ['BOOTY']
    initialize_booty(booty)

if __name__ == '__main__':
    main()
