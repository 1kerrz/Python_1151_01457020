def cola(x):
    dcola, dbottle = x,x
    while True:
        if dbottle == 2:
            dcola += 1
            break
        elif dbottle < 2:
            break
        else:
            temp = dbottle//3
            dcola += temp
            dbottle = dbottle%3 + temp
    return dcola

while True: 
    try:
        x = int(input())
        print(cola(x))
    except EOFError:
        break
    

