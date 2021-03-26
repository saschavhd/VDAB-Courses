from collections import defaultdict

dic = defaultdict(int)

for el in input("Enter a sentence: ").lower():
    if el.isalpha():
        dic[el] += 1

for k, v in sorted(dic.items()):
    print("Letter {} - Frequence {}".format(k, v))
