array1 = [1, 5, 4, 6]
array2 = [1, 6, 1, 6]
multipliers = [1, 2, 3, 4, 5, 6]

for multiplier1 in multipliers:
    for multiplier2 in multipliers:
        result = [(x * multiplier1 + y * multiplier2) % 7 for x, y in zip(array1, array2)]
        print(result)