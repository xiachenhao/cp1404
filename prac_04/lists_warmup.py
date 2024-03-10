numbers = [3, 1, 4, 1, 5, 9, 2]

# Predictions:
# numbers[0] will be 3
# numbers[-1] will be 2
# numbers[3] will be 1
# numbers[:-1] will be [3, 1, 4, 1, 5, 9]
# numbers[3:4] will be [1]
# 5 in numbers will be True
# 7 in numbers will be False
# "3" in numbers will be False
# numbers + [6, 5, 3] will be [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)
