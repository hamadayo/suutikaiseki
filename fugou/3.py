def calculate_birthday_probability(n):
    if n < 2:
        return 0.0

    probability = 1.0
    for i in range(2, n + 1):
        probability *= (365 - (i - 1)) / 365

    return 1 - probability

target_probability = 0.97
num_people = 2

while True:
    probability = calculate_birthday_probability(num_people)
    if probability >= target_probability:
        break
    num_people += 1

print("同じ誕生日の人が2人以上存在する確率が90%以上になるためには、最低", num_people, "人集まればよいです。")
