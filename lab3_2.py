car_num = int(input())

while True:
    check=1
    target = list(map(int,input().split()))
    stack = []
    if target[0]==0:
        break
    point = target[0]
    for i in range(car_num):
        if target[i]>point:
            for j in range(point+1,target[i]):
                stack.append(j)
        elif target[i]<point:
            pop = stack.pop()
            if target[i]!=pop:
                print("NO")
                check=0
                break
        else:
            stack = list(range(1, target[i]))
        point = target[i];
    if check==1:
        print("YES")
        