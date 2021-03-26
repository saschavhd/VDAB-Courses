from collections import defaultdict

dic = defaultdict(int)
inp = input("Enter a word: ").lower()
for el in inp:
    dic[el] += 1

for k, v in sorted(dic.items()):
    print("Letter {} - Frequency {}".format(k, v))
