# リストをスライス
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# スライスによるループ
players = ["charles", "martina", "michael", "florence", "eli"]

print("チームの最初の3人です。")
for player in players[:3]:
	print(player.title())