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