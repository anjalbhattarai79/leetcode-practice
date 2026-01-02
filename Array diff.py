'''
f a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
'''

def array_diff(a, b):
    if not a or not b:
        return a
    final_list = []
    for i in a:
        if i not in b:
            final_list.append(i)
            
    return final_list