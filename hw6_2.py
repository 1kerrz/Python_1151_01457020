from decimal import Decimal, ROUND_HALF_UP
times = int(input())
score = []

try:
    for i in range(times):
        try:
            data = input().split(',')
            if len(data) != 2 or not data[0] or any(c.isspace() for c in data[0]):
                raise BufferError()
            num = float(data[1])
            if not num.is_integer() or num < 0 or num > 100:
                raise ValueError()
        except BufferError:
            print("Error: invalid data format")
        except ValueError:
            print("Error: invalid score")
        else:
            score.append(int(num))
            print("OK")
finally:
    if len(score) == 0:
        print("No valid scores")
    else:
        total = 0
        for i in score:
            total += i
        avg = Decimal(str(total))/len(score)
        rst = avg.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        print(f"Average score: {rst}")
