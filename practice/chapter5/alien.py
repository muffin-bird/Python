# 演習問題 5-3
alien_color = "黄"

if alien_color == "緑":
	print("プレイヤーが5点を獲得した")

alien_color = "緑"

if alien_color == "緑":
	print("プレイヤーが5点を獲得した")

# 演習問題 5-4
alien_color = "赤"

if alien_color == "緑":
	print("プレイヤーが5点を獲得した")
else:
	print("プレイヤーが10点を獲得した")

# 演習問題 5-5
alien_color = "赤"

if alien_color == "緑":
	print("プレイヤーが5点を獲得した")
elif alien_color == "黄":
	print("プレイヤーが10点を獲得した")
else:
	print("プレイヤーが15点を獲得した")

alien_color = "黄"

if alien_color == "緑":
	print("プレイヤーが5点を獲得した")
elif alien_color == "黄":
	print("プレイヤーが10点を獲得した")
else:
	print("プレイヤーが15点を獲得した")

alien_color = "緑"

if alien_color == "緑":
	print("プレイヤーが5点を獲得した")
elif alien_color == "黄":
	print("プレイヤーが10点を獲得した")
else:
	print("プレイヤーが15点を獲得した")

# 演習問題 5-6
age = 12

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