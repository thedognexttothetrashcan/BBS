# you are wang -> wang are you

# this is a string -> string a is this


def foo(line):
    words = line.split(' ')
    words = words[::-1]
    return ' '.join(words)


# ['you', 'are', 'wang']

# ['this', 'is', 'a', 'string']
#     0     1     2        3


#            1   length - 2
# 0 3
# length - 1

def bar(line):
    '''原地反转'''
    words = line.split(' ')
    length = len(words)
    for i in range(length // 2):
        other_index = length - i - 1
        words[i], words[other_index] = words[other_index], words[i]
    return ' '.join(words)
