import time, redis
import yaml

cache = redis.Redis(host='127.0.0.1', port=6379)

def get_hit_counts():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


def get_configs():
    with open("config.yaml", "r") as stream:
        try:
            data = yaml.safe_load(stream)["database"]
            username = data["username"]
            password = data["password"]
            dbname = data["dbname"]
        except yaml.YAMLError as exc:
            print(exc)
    return username, password, dbname
