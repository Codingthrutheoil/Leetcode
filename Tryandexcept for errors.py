while True:
    try:
        value = int(input('Please enter an integer: '))
        print('The reciprocal of', value, 'is', 1/value)
        break
    except ValueError:
        print('That is not an integer. Please enter an integer:')
    except ZeroDivisionError:
        print('Division by zero is not allowed in our Universe.')