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