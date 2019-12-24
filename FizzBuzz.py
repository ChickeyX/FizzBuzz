for x in range(1, 101):
    response = ''
    if x % 3 == 0:
        response += 'Fizz'
    if x % 5 == 0:
        response += 'Buzz'
    print(response or x)
