if __name__ == '__main__':
    str1 = raw_input()
    compressed_string = ''
    print str1
    count = 1
    for i in range(len(str1)):
        if i+1 < len(str1) and str1[i] == str1[i+1]:
            count += 1
        else:
            compressed_string += str1[i] + str(count)
            count = 1
    print compressed_string