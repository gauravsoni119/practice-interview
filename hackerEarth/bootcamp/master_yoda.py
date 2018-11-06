def master_yoda(text):
    return ' '.join(text.split(' ')[::-1])
print master_yoda('I am home')
print master_yoda('We are ready')