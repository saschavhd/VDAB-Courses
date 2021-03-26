from random import randint


class multiDimArr():

    def __init__(self, n):
        self.dimSize = n
        self.arr = self.createArr()

    def createArr(self):
        arr = []
        for _ in range(self.dimSize):
            temp = []
            for _ in range(self.dimSize):
                temp.append(randint(0, 99))
            arr.append(temp)
        return arr

    def getAverageOfColumn(self, i):
        avg = 0
        for k in range(self.dimSize):
            avg += self.arr[k][i-1]
        avg /= self.dimSize
        return avg

    def getArray(self):
        return self.arr


if __name__ == '__main__':
    myArr = multiDimArr(int(input("Enter dimension size: ")))

    print(myArr.getArray())
    print(myArr.getAverageOfColumn(int(input("Enter column number (1-{}): ".format(myArr.dimSize)))))
