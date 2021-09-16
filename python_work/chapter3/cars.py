# リストをアルファベット順に変更
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

# リストをアルファベット逆順に変更
cars.sort(reverse=True)
print(cars)

# 文字列が日本語
cars = ["bmw", "アウディ", "日産", "すばる"]
cars.sort()
print(cars)

# リストを一時的にソートする
cars = ["bmw", "audi", "toyota", "subaru"]
print("元のリスト")
print(cars)
print("\nソートされたリスト")
print(sorted(cars))
print("\n元のリストを再表示")
print(cars)