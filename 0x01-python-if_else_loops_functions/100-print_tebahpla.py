def print_tebahpla():
    for i in range(25, -1, -1):
        print("{:c}{:c}".format(122 - i * 2, 90 - i * 2), end='')

print_tebahpla()
