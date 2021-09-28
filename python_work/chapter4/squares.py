squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares)

# 簡潔
squares = []
for value in range(1, 11):
	squares.append(value ** 2)

print(squares)

# リスト内包表記
squares = [value ** 2 for value in range(1, 11)]
print(squares)