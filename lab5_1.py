def add(*args):
    total = 0
    for i in args:
        if i%2 == 0:
            total += i

    return total

while True:
    x = input().split()
    if x[0]=='END':
        break;

    x = map(int, x)
    print(add(*x))