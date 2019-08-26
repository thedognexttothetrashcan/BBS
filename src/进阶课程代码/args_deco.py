'''定义一个装饰器，打印出被装饰函数的执行 N 次的时间'''

import time


def timer(times):
    def deco(func):
        def wrap(*args, **kwargs):
            t0 = time.time()
            for i in range(times):
                result = func(*args, **kwargs)
            t1 = time.time()
            print(t1 - t0)
            return result
        return wrap
    return deco


@timer(100000)
def foo(x, y):
    return x ** y


def bar(x, y):
    return x ** y


# 带参数装饰器拆解过程
deco = timer(10000000)
bar = deco(bar)

# 单行写法
timer(100000)(bar)(3, 4)

# 执行
bar(3, 4)
