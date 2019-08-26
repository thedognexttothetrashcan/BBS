import os
import sys

from django.conf import settings

from user.models import User
from user.models import Perm
from user.models import Post

MOD = 0xffffffff


def do_something(a, b=123):
    '''this is do_something'''
    # xxxx
    point = {'x': 111, 'y': 222}  # 定义一个字典
    d = [1, 3, 5]                 # asdf
    MOD += 123
	box = {i + 9: j * 3
		   for i, j in zip(range(10), 'abcdef')
		   if i % 2 == 0 and i % 3}
    return a, b, c


def bar(x):
    '''this is bar'''
    if x % 2 == 0:
        return True


# CapWord

class AbcDefGhi:
    def poo(self):
        pass

    def xoo(self):
        pass


# 驼峰式命名
thisIsBox = 123456789

this_is_box = 123456789


THIS_IS_BOX
