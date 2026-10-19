def carry_ct(a,b):
    ct = 0
    icarry = 0
    while a>0 or b>0:
        if (a%10)+(b%10)+icarry >= 10:
            ct+=1
            icarry = 1
        else:
            icarry = 0
        a//=10
        b//=10
    return ct

while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break;
    carry = carry_ct(a,b)

    if carry==0:
        print("No carry operation.")
    elif carry==1:
        print("1 carry operation.")
    else:
        print(f"{carry} carry operations.")
