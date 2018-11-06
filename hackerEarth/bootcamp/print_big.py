a = {'a': '  *  ', 'c': ' * * ', 'b': '*****', 'd': '*   *', 'e': '*   *'}
print a
def print_big(pattern):
    for key in pattern:
        print a[key]
print_big(a)