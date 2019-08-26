'''多层装饰器'''

def deco1(func):
    print('enter deco1(%s)' % func.__name__)
    def wrapper1(*args, **kwargs):
        print('enter wrapper1')
        result = func(*args, **kwargs)
        print('exit  wrapper1')
        return result
    print('exit  deco1')
    return wrapper1


def deco2(func):
    print('enter deco2(%s)' % func.__name__)
    def wrapper2(*args, **kwargs):
        print('enter wrapper2')
        result = func(*args, **kwargs)
        print('exit  wrapper2')
        return result
    print('exit  deco2')
    return wrapper2


def deco3(func):
    print('enter deco3(%s)' % func.__name__)
    def wrapper3(*args, **kwargs):
        print('enter wrapper3')
        result = func(*args, **kwargs)
        print('exit  wrapper3')
        return result
    print('exit  deco3')
    return wrapper3


@deco1
@deco2
@deco3
def foo(x, y):
    return x ** y

print('---------- 装饰过程结束')

# 执行被装饰函数
foo(3, 4)

print('==================================================')

def bar(x, y):
    return x ** y


# 多层装饰器: 装饰过程的拆解
wrapper3 = deco3(bar)
wrapper2 = deco2(wrapper3)
wrapper1 = deco1(wrapper2)
bar = wrapper1

# 单行写法:
# bar = deco1( deco2( deco3( bar ) ) )

print('---------- 装饰过程结束')

# 执行被装饰函数
n = bar(3, 4)
