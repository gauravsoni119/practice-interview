import re
string = raw_input()
rotation_num = input()
encrypted_string = ''
for s in range(len(string)):
    if re.search(r'([a-zA-Z0-9])', string[s]) is not None:
        encrypted_string += chr(ord(string[s]) + rotation_num)
    else:
        encrypted_string += string[s]
print encrypted_string

