# 文字列
print("私は友達に'好きな言語はPythonです!'と言った。")
print('プログラミング言語"Python"の名前はヘビではなくモンティ・パイソンから来ています。')
print("Python's strengths (Pythonの強み)は多様で協力的なコミュニティーです。")

# 空白文字
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 文字列の右側の空白文字を削除
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# 左側の空白文字を削除
favorite_language = ' python'
favorite_language = favorite_language.lstrip()
print(favorite_language)

# 左右両方の空白文字を削除
favorite_language = ' python '
favorite_language = favorite_language.strip()
print(favorite_language)