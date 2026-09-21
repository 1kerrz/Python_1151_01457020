n, m = map(int, input().split())
aFriend = set(map(int, input().split()))
bFriend = set(map(int, input().split()))
commonFriend_set = aFriend & bFriend
commonFriend = sorted(list(commonFriend_set))

print(len(commonFriend))
if commonFriend:
    for i in commonFriend:
        print(i,end=" ")

