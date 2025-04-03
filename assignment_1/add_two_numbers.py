input('Input: number1 number2\n')

try: a, b = c.split(' ');a = float(a);b = float(b);print('added {} and {} equal {}'.format(a, b, a+b));print('subtracted {} from {} equals {}'.format(a, b, a-b));print('multiplied {} to {} equals {}'.format(a, b, a*b));print('dividing {} from {} equals'.format(a, b, a/b))
except Exception as e: print("Invalid input!");print('a == {}, b == {}, c == {}'.format(a, b, c))