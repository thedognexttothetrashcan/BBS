import time


class retry(object):
    def __init__(self, max_retries=3, wait=0, exceptions=(Exception,)):
        self.max_retries = max_retries
        self.exceptions = exceptions
        self.wait = wait

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.max_retries + 1):
                try:
                    result = func(*args, **kwargs)
                except self.exceptions:
                    print('retry...')
                    time.sleep(self.wait)
                    continue
                else:
                    return result
        return wrapper


import random

@retry(3, 1, (ValueError,))
def foo(n1, n2):
    n = random.randint(n1, n2)
    if n < 0:
        raise ValueError('n < 0')
    return n


n = foo(-10, 5)
print(n)
