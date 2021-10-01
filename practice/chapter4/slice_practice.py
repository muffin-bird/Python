# 演習問題 4-10
print("リストの最初の3つの要素です。")
numbers = list(range(1, 10))
for number in numbers[:3]:
	print(number)

print("\nリストの中央の3つの要素です。")
for number in numbers[3:6]:
	print(number)

print("\nリストの最後の3つの要素です。")
for number in numbers[-3:]:
	print(number)

# 演習問題 4-11
pizzas = ["tomato", "cheese", "honey"]
friend_pizzas = pizzas[:]

pizzas.append("chili")
friend_pizzas.append("seafood")

print("\n私の好きなpizza")
for pizza in pizzas:
	print(pizza)

print("\n友達が好きなpizza")
for friend_pizza in friend_pizzas:
	print(friend_pizza)