# 演習問題 4-3
for value in range(1, 21):
	print(value)

# 演習問題 4-4
for value in range(1, 1_000_001):
	print(value)

# 演習問題 4-5
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 演習問題 4-6
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
	print(number)

# 演習問題 4-7
three_numbers = list(range(3, 31, 3))
for number in three_numbers:
	print(number)

# 演習問題 4-8
cubic_numbers = []
for number in range(1, 11):
	cubic_numbers.append(number ** 3)

for number_2 in cubic_numbers:
	print(number_2)

# 演習問題 4-9
cubic_numbers = [number ** 3 for number in range(1, 11)]
print(cubic_numbers)