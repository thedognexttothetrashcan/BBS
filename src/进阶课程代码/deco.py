import random


def check(func):
    '''检查原函数返回值，确保是一个非负数，如果是负数，将结果修改为 0'''
    def wrapper(*args, **kwargs):
        '''this is wrapper'''
        result = func(*args, **kwargs)
        if result < 0:
            result = 0
        return result
    return wrapper


@check
def foo(n0, n1):
    '''this is foo'''
    return random.randint(n0, n1)


def bar(n0, n1):
    '''this is bar'''
    return random.randint(n0, n1)

bar = check(bar)
