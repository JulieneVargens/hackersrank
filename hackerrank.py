def test(n):
    resto = n % 2
    if resto != 0:
        print('Weird')
    elif n==range(2,5):
        print('Not Weird')
    elif n==range(6,20):
        print('Weird')
    elif n>=20:
        print('Not Weird')
test(24)