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

wrapper = check(foo)
foo = wrapper
foo(-10, 10)


class Check:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        '''this is __call__'''
        result = self.func(*args, **kwargs)
        if result < 0:
            result = 0
        return result


@Check
def bar(n0, n1):
    '''this is foo'''
    return random.randint(n0, n1)

obj = Check(bar)
bar = obj
bar(-10, 10)
