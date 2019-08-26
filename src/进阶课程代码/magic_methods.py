
__init__


class A:
    def __new__(cls):

    def __init__(self):
        self.x = 123


a = A()

python
    连接池
| | | |
V V V V
MySQL



    str list tuple dict set
+     v    v     v    x   x   __add__
-     x    x     x    x   v   __sub__
*     v    v     v    x   x   __mul__
/     x    x     x    x   x   __truediv__



for: __iter__
len: __len__
in: __contains__
