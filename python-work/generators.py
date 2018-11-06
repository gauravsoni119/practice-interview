def create_cubes(n):
    for i in range(n):
        yield i**3

for x in create_cubes(10):
    print x

def gen_fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in gen_fib(10):
    print num


def gen_seq(n):
    for i in range(n):
        yield i

g = gen_seq(5)
print next(g)
print next(g)

s = 'Hello World'
iterator = iter(s)
print next(iterator)