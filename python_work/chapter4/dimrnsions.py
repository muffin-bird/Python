# タプル
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# ループ
for dimension in dimensions:
	print(dimension)

# タプル上書き
dimensions = (200, 50)
print("元のサイズ")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\n変更したサイズ")
for dimension in dimensions:
	print(dimension)