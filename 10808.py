s = str(input())

alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
word = [ ]

for str in s:
    word.append(str)

for str in alp:
    print(word.count(str), end = " ")
