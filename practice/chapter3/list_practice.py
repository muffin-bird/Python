# 演習問題 3-1
names = ["muffin", "police", "milk"]
print(names[-2])

# 演習問題 3-2
print(f"こんにちは{names[0]}!")
print(f"こんにちは{names[1]}!")
print(f"こんにちは{names[2]}!")

# 演習問題 3-3
carbrands = ["Honda", "Toyota", "suzuki"]
print(f"私は{carbrands[1]}の車がほしい。")

# 演習問題 3-4
persons = ["muffin", "milk", "police"]

name = persons[0]
print(f"こんにちは{name}さん、夕食はいかがでしょうか。")
name_2 = persons[1]
print(f"こんにちは{name_2}さん、夕食はいかがでしょうか。")
name_3 = persons[2]
print(f"こんにちは{name_3}さん、夕食はいかがでしょうか。")

# 演習問題 3-5
print(f"{name_2}さんが夕食に参加できないとのことです")
del persons[1]
persons.insert(1, "vanilla")
name = persons[0]
print(f"こんにちは{name}さん、夕食はいかがでしょうか。")
name_2 = persons[1]
print(f"こんにちは{name_2}さん、夕食はいかがでしょうか。")
name_3 = persons[2]
print(f"こんにちは{name_3}さん、夕食はいかがでしょうか。")

# 演習問題 3-6
print("大きなテーブルを見つけました。")
persons.insert(0, "chocolate")
persons.insert(2, "pine")
persons.append("peach")
print(persons)
name = persons[0]
print(f"こんにちは{name}さん、夕食はいかがでしょうか。")
name_2 = persons[1]
print(f"こんにちは{name_2}さん、夕食はいかがでしょうか。")
name_3 = persons[2]
print(f"こんにちは{name_3}さん、夕食はいかがでしょうか。")
name_4 = persons[3]
print(f"こんにちは{name_4}さん、夕食はいかがでしょうか。")
name_5 = persons[4]
print(f"こんにちは{name_5}さん、夕食はいかがでしょうか。")
name_6 = persons[5]
print(f"こんにちは{name_6}さん、夕食はいかがでしょうか。")

# 演習問題 3-7
print("申し訳ございません。夕食には2人の席しかございませんでした。")
name_6 = persons.pop()
print(f"{name_6}さん、夕食は中止になりました。申し訳ございません。")
name_5 = persons.pop()
print(f"{name_5}さん、夕食は中止になりました。申し訳ございません。")
name_4 = persons.pop()
print(f"{name_4}さん、夕食は中止になりました。申し訳ございません。")
name_3 = persons.pop()
print(f"{name_3}さん、夕食は中止になりました。申し訳ございません。")
print(persons)
name = persons[0]
print(f"こんにちは{name}さん、夕食にきてください")
name_2 = persons[1]
print(f"こんにちは{name_2}さん、夕食にきてください")
del persons[0]
del persons[0]
print(persons)