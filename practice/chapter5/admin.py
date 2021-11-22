# 演習問題 5-8
users = ["muffin", "milk", "police", "rocket", "admin"]

for user in users:
	if user == "admin":
		print("こんにちはadmin、状況のレポートを見ますか？")
	else:
		print(f"こんにちは{user}、またログインしてくれてありがとう。")

# 演習問題 5-9

users = []

if users:
    for use in users:
        if user == 'admin':
            print("こんにちはadmin、状況のレポートを見ますか？")
        else:
            print(f"こんにちは{user}、またログインしてくれてありがとう。")
else:
    print("ユーザー募集中です！")

# 演習問題 5-10
current_users = ["muffin", "milk", "rocket", "police", "island"]

new_users = ["Muffin", "Milk", "Remon", "MyMan", "Batter"]

new_users_lower = [new_user_lower.lower() for new_user_lower in current_users]

for new_user in new_users:
    if new_user.lower() in new_users_lower:
        print(f"{new_user}は利用できないため、別のユーザー名を入力してください！")
    else:
        print(f"{new_user}、ユーザー名は利用可能です！")

# 演習問題 5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

# 演習問題 5-12
# 演習問題 5-6の修正
ages = [1, 5, 10, 15, 20, 30]

for age in ages:
    if age < 2:
        print("赤ちゃん")
    elif age < 4:
        print("幼児")
    elif age < 13:
        print("子供")
    elif age < 20:
        print("ティーンエイジャー")
    elif age < 65:
        print("大人")
    else:
        print("高齢者")