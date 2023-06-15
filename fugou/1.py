numbers = [1, 6, 1, 6]
multipliers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    for multiplier in multipliers:
        result = (number * multiplier) % 7
        print(result, end=' ')
    print()
