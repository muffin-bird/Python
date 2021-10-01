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

# 演習問題 4-12
my_foods = ["ピザ", "だんご", "ケーキ"]
friend_foods = my_foods[:]

my_foods.append("チョコレート")
friend_foods.append("アイスクリーム")

print("\n私の好きな食べ物リスト")
for my_food in my_foods:
	print(my_food)

print("\n友達が好きな食べ物リスト")
for friend_food in friend_foods:
	print(friend_food)