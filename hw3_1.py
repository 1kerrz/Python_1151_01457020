n = int(input())

for i in range(n):
    sentence = str(input())
    ct = {}
    for char in sentence:
        if char in ct:
            ct[char] += 1
        else:
            ct[char] = 1
    max_char = max(ct, key=ct.get)
    print(max_char)