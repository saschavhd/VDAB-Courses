alp = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def getValidKeyWord():
    inp = input("Enter a keyword: ").lower()
    for el in inp:
        if not el.isalpha():
            return getValidKeyWord()
    return inp


def getValidSentence():
    inp = input("Enter a sentence: ").lower()
    for el in inp:
        if not el.isalpha() and el != ' ':
            return getValidSentence()
    return inp


def encode(keyWord, str):
    extendedKeyWord = ''
    res = [0] * len(str)
    while (len(extendedKeyWord) < len(str)):
        extendedKeyWord += keyWord
    while (len(extendedKeyWord) > len(str)):
        extendedKeyWord = extendedKeyWord[:-1]
    for i in range(len(str)):
        res[i] = (alp.index(str[i]) + alp.index(extendedKeyWord[i])) % 27
    return res


def decode(keyWord, encryption):
    pass


if __name__ == '__main__':
    key = getValidKeyWord()
    sentence = getValidSentence()

    crypt = encode(key, sentence)
    print(crypt)
