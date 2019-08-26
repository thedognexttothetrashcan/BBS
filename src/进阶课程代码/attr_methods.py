class TestClass:
    z = [7,8,9]

    def __init__(self):
        self.money = 123456
        self.x = 10000
        self.y = 'abc'

    def foo(self, x, y):
        return x ** y

    def __setattr__(self, name, value):
        if name == 'x' and not isinstance(value, int):
            raise TypeError('x must be int')

        if name == 'money' and value < 0:
            raise ValueError('money < 0')
        object.__setattr__(self, name, value)

        print('set %s = %s' % (name, value))

    def __getattribute__(self, name):
        print('getattribute %s' % name)
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        print('getattr %s' % name)
        return -1
