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