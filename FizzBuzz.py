for x in range(1, 101):
    string = ''
    if x % 3 == 0:
        string += 'Fizz'
    if x % 5 == 0:
        string += 'Buzz'
    print(x if not string else string)
