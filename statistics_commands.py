from collections import Counter

def findMean(newList):
    totalElements = len(newList)
    total = 0

    for i in (newList):
        total += i

    print('\nThe mean is: ')
    print(total / totalElements)

def findMedian(newList):
    if len(newList)%2==0:
        n = len(newList)//2
        median = (newList[n-1] + newList[n])/2 
    else: 
        median = newList[len(newList)//2]

    print('\nThe median is: ')
    print(median)

def findMode(newList):
    freqDict = Counter(newList)

    maxNumCount = max(freqDict.values())

    mode = [i for i, j in freqDict.items() if j == maxNumCount]

    if len(mode) == 1:
        print('\nThe mode is : ')
        print(mode[0])
    else:
        print('\nThe mode is : ')
        print(mode)

def findRange(newList):
    print('\nThe range is:')
    print(max(newList)-min(newList))


maxNum = int(input('Number of elements: '))

oldList = [True] * (maxNum)

print('Enter all individual elements:\n')

for i in range(maxNum):
    oldList[i] = int(input())

newList = sorted(oldList)

print(f'Original list: {oldList}\nSorted list: {newList}')

findMean(newList)

findMedian(newList)

findMode(newList)

findRange(newList)