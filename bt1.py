a = int(input())
b = int(input())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

print(gcd(a, b))