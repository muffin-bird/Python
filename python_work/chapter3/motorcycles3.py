# リストから要素を削除する
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# リスト中の任意の要素を削除 (del文)
del motorcycles[0]
del motorcycles[1]
print(motorcycles)

# リストの最後の要素を削除しその要素を使用できる (popメソッド)
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 最近入手したバイク (例)
motorcycles = ["honada", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print(f"最近手に入れたバイクは{last_owned.title()}です。")

# リスト中の任意の要素を削除 (popメソッド)
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print(f"最近手に入れたバイクは{first_owned.title()}です。")

# リスト中の削除したい値の位置が不明の場合 (removeメソッド)
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

# 削除した値を使用 (removeメソッド)
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()}は私には高すぎます。")
