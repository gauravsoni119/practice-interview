def paper_doll(text):
    return ''.join(map(lambda x: x*3, text))

print paper_doll('Hello')
print paper_doll('Mississippi')