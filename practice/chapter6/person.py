# 演習問題 6-1
person = {
	'first_name': 'muffin',
	'last_name': 'man',
	'age': 47,
	'city': 'osaka'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 演習問題 6-2
favorite_numbers = {
	'muffin': 10,
	'milk': 20,
	'police': 30,
	'island': 40,
	'myman': 50
}

number= favorite_numbers['muffin']
print(f"muffinの好きな数字は{number}です。")

number= favorite_numbers['milk']
print(f"milkの好きな数字は{number}です。")

number= favorite_numbers['police']
print(f"policeの好きな数字は{number}です。")

number= favorite_numbers['island']
print(f"islandの好きな数字は{number}です。")

number= favorite_numbers['myman']
print(f"mymanbの好きな数字は{number}です。")

# 演習問題 6-3
glossary = {
    'string': '文字列',
    'comment': 'コメントをする',
    'list': '要素の集まり',
    'variable': '値を入れる箱',
    'print': "画面に出力する"
}

explannation = 'string'
print(f"{explannation.title()}: {glossary[explannation]}")

explannation = 'comment'
print(f"\n{explannation.title()}: {glossary[explannation]}")

explannation = 'list'
print(f"\n{explannation.title()}: {glossary[explannation]}")

explannation = 'variable'
print(f"\n{explannation.title()}: {glossary[explannation]}")

explannation = 'print'
print(f"\n{explannation.title()}: {glossary[explannation]}")