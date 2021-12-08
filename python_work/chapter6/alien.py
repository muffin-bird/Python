# シンプルな辞書
alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

# 辞書の値にアクセスする
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])

new_points = alien_0["points"]
print(f"{new_points}点獲得しました!")

# 新しいキーと値のペアを追加する
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# 空の辞書から開始する
alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)