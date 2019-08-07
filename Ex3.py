#Generate 500 random numbers and create a method to print the nth smallest number in a programming language of your choice

import random

class Example2():

    def GenerateNumbers(self):

        entry = 500
        randomList = []

        for i in range(entry):
            randomList.append(random.randint(i+1, 1000))

        print("Random List: " + str(randomList))
        randomList.sort()

        smallestNumber = int(input("Enter nth smallest number: "))
        print(randomList[smallestNumber-1])



if __name__ == '__main__':
    Example = Example2()
    try:
        Example.GenerateNumbers()
    except Exception as e:
        print(str(e))