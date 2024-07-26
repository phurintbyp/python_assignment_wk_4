grades = [55, 70, 65, 40, 90, 85, 50, 77]

passed_with_bonus = list(map(lambda x: x * 1.05, filter(lambda x: x >= 60, grades)))

print(passed_with_bonus)