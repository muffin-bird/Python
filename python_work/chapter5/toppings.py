# 演算子 (!=)
requested_topping = "マッシュルーム"

if requested_topping != "アンチョビ":
	print("アンチョビを注文してください!")

# inキーワード
requested_topping = ["マッシュルーム", "オニオン", "パイナップル"]

print("マッシュルーム" in requested_topping)
print("ペパロニ" in requested_topping)

# 複数の条件をテストする
requested_toppings = ["マッシュルーム", "エクストラチーズ"]

if "マッシュルーム" in requested_toppings:
	print("マッシュルームを追加する。")
if "ペパロニ" in requested_toppings:
	print("ペパロニを追加する。")
if "エクストラチーズ" in requested_toppings:
	print("エクストラチーズを追加する。")

print("\nピザができました!")

# forループ
requested_toppings = ["マッシュルーム", "ピーマン", "パイナップル"]

for requested_topping in requested_toppings:
	print(f"ピザに{requested_topping}を追加します。")

print("\nピザができました!")

requested_toppings = ["マッシュルーム", "ピーマン", "パイナップル"]

for requested_topping in requested_toppings:
	if requested_topping == "ピーマン":
		print("ピーマンは品切れです。")
	else:
		print(f"ピザに{requested_topping}を追加します。")

print("\nピザができました!")

# リストが空でないことを確認する
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"トッピングに{requested_topping}を追加します。")
	print("\nピザができました!")
else:
	print("プレーンピザでよろしいでしょうか？")

# 複数のリストを使用する
available_toppings = ["マッシュルーム", "オリーブ", "ピーマン","ペパロニ", "パイナップル", "エクストラチーズ"]

requested_toppings = ["マッシュルーム", "エクストラチーズ", "フライドポテト"]

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"ピザに{requested_topping}を追加します。")
	else:
		print(f"申し訳ありません、{requested_topping}はありません。")

print("\nピザができました!")