def is_even(number):
    last_digit = str(number)[-1]
    if int(last_digit) % 2 == 0:
        return True
    else:
        return False

assert is_even(2**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')
