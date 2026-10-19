ct=0
try:
    try:
        ans = float(input())
        if not ans.is_integer():
            raise ValueError("int")
        if ans < 0 or ans > 50:
            raise ValueError("range")
    except ValueError as e:
        if str(e) == "int":
            print("Error: please enter an integer")
        elif str(e) == "range":
            print("Error: number out of range")
        else:
            print("Error: please enter a number")
        raise SystemExit
    else:
        while True:
            try:
                ct+=1
                guess = float(input())
                if not guess.is_integer():
                    raise ValueError("int")
                if guess < 0 or guess > 50:
                    raise ValueError("range")
            except ValueError as e:
                if str(e) == "int":
                    print("Error: please enter an integer")
                elif str(e) == "range":
                    print("Error: number out of range")
                else:
                    print("Error: please enter a number")
            else:
                if guess < ans:
                    print("You are too low!")
                elif guess > ans:
                    print("You are too high!")
                else:
                    print("You got it!")
                    break
            finally:
                pass
finally:
    print(f"You guessed {ct} times.")
    