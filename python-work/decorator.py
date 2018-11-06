def hello(name = 'john'):
    print 'The hello() has been executed'

    def greet():
        return '\t This is greet function inside hello'
    
    def welcome():
        return '\t This is welcome function inside hello'

    print 'Returing functions from inside hello()'

    if name == 'john':
        return greet
    else:
        return welcome

my_func = hello('john')

print my_func()

def test(some_fun):
    print 'Calling helle function'
    some_fun()

test(hello)

def validate_input(func):
    def wrapper_func():
        print 'Checking if inputs are valid number or not'
        func()
        print 'Calling after func executed'
    return wrapper_func

@validate_input
def sum():
    print 1 + 1
    #return 1 + 1
sum()

