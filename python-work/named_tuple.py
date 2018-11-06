from collections import namedtuple

t = namedtuple('Dog', 'name age')
dog = t(name ='Lab', age = 20)
print dog.name, dog.age