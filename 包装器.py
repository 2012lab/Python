from functools import wraps
import time


def timethis(x):
    @wraps(x)
    def wrapper(*args, **kwargs):
        start = time.time()
        x(*args, **kwargs)
        end = time.time()
        cost = end - start
        print(x.__name__, cost)
    return wrapper


@timethis
def countDown(n):
    while(n>0):
        n= n-1

countDown(10000000)
