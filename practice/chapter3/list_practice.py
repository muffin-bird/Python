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