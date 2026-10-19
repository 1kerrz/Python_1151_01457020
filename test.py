from decimal import Decimal, ROUND_HALF_UP

N = int(input())
scores = []

for _ in range(N):
    try:
        data = input().split(',')

        if len(data) != 2:
            raise BufferError

        score = int(data[1])

        if not 0 <= score <= 100:
            raise ValueError

    except BufferError:
        print("Error: invalid data format")

    except ValueError:
        print("Error: invalid score")

    else:
        scores.append(score)
        print("OK")

if len(scores) == 0:
    print("No valid scores")
else:
    avg = Decimal(sum(scores)) / Decimal(len(scores))
    avg = avg.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )
    print(f"Average score: {avg:.2f}")