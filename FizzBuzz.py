for i in range(1, 101):
    response = ''
    if i % 3 == 0:
        response += 'Fizz'
    if i % 5 == 0:
        response += 'Buzz'
    print(response or i)
