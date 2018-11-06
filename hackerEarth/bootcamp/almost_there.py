def almost_there(n):
    if ((n in range(100, 111)) or (n in range(200, 211))):
        return True
    return False
print almost_there(200)
print almost_there(205)
print almost_there(211)
print almost_there(100)
print almost_there(110)
print almost_there(111)
print almost_there(105)