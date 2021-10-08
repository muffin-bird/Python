# 演算子 (!=)
requested_topping = "マッシュルーム"

if requested_topping != "アンチョビ":
	print("アンチョビを注文してください!")

# inキーワード
requested_topping = ["マッシュルーム", "オニオン", "パイナップル"]

print("マッシュルーム" in requested_topping)
print("ペパロニ" in requested_topping)