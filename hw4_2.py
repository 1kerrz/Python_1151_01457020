def Palindrome(word):
    left = 0
    right = len(word)-1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def Mirrow(word):
    normal_mirrow_set = {'A','H','I','M','O','T','U','V','W','X','Y','1','8'}
    special_mirrow_dict = {
        'E': '3',
        'J': 'L',
        'S': '2',
        'Z': '5'
    }

    def mirrow_check(a, b):
        if a == b:
            return a in normal_mirrow_set
        if special_mirrow_dict.get(a) == b:
            return True
        if special_mirrow_dict.get(b) == a:
            return True
        return False
    left = 0
    right = len(word)-1
    while left <= right:
        if not mirrow_check(word[left],word[right]):
            return False
        left += 1
        right -= 1
    return True

while True:
    try:
        word = input().strip()
    except EOFError:
        break
    if word == "":
        continue

    is_palindrome = Palindrome(word)
    is_mirror = Mirrow(word)

    if is_palindrome and is_mirror:
        print(f'{word} -- is a mirrored palindrome.')
    elif is_palindrome and not is_mirror:
        print(f'{word} -- is a regular palindrome.')
    elif not is_palindrome and is_mirror:
        print(f'{word} -- is a mirrored string.')
    else:
        print(f'{word} -- is not a palindrome.')
    print()