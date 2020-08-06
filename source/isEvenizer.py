with (open('isEven.py', 'w')) as file:
    file.write('def isEven(n):\n');
    is_even = False
    file.write('    if (n == 1):\n')
    file.write('        return {}\n'.format(is_even))
        
    for i in range(2, 500001):
        is_even = (i % 2 == 0)

        file.write('    elif (n == {}):\n'.format(i))
        file.write('        return {}\n'.format(is_even))
        
