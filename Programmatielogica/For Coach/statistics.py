from random import randint


def createRandomData():
    arr = []
    for i in range(5, randint(6, 100)):
        arr.append(randint(100, 199))
    return arr


class statArr():

    def __init__(self, arr):
        self.arr = arr
        self.avg = sum(self.arr)/len(self.arr)
        self.sigma = self.calculateSD()

    def withinOneSD(self):
        temp = []
        for el in self.arr:
            print(el)
            if self.avg - self.sigma <= el <= self.avg + self.sigma:
                temp.append(el)
        return temp

    def withinOneAndTwoSD(self):
        temp = []
        for el in self.arr:
            print(el)
            if self.avg - self.sigma * 2 <= el < self.avg - self.sigma or self.avg + self.sigma < el <= self.avg + self.sigma * 2:
                temp.append(el)
        return temp

    def calculateSD(self):
        powerSum = 0
        for el in self.arr:
            powerSum += ((el-self.avg)**2)
        return (powerSum/len(self.arr)) ** (1/2)


if __name__ == '__main__':
    test = statArr([5,5,10,10])
    print("Data: {}".format(test.arr))
    print("Average: {}".format(round(test.avg, 2)))
    print("Standard Deviation: {}".format(round(test.sigma, 2)))
    print("Data within one SD: {}".format(test.withinOneSD()))
    print("Data between one and two SD: {}".format(test.withinOneAndTwoSD()))
