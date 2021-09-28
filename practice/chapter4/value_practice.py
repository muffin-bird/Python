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