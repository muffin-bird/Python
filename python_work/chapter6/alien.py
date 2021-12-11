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

# 辞書の値を変更する
alien_0={'color':'green'}
print(f"エイリアンは{alien_0['color']}です。")

alien_0['color']='yellow'
print(f"エイリアンは{alien_0['color']}になりました。") 

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
alien_0['speed'] = 'fast'

print(f"最初のX座標:{alien_0['x_position']}")

# エイリアンは右に移動します
# 現在のスピードによってエイリアンの移動距離を決定します・
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# 素早いエイリアン
	x_increment = 3

# 新しい位置は元の位置に移動距離を加算します。
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"新しいX座標: {alien_0['x_position']}")

# キーと値のペアを削除する
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0['points']
print(alien_0)