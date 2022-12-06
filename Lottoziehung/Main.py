from random import randint

list_return = []

def get_random_six(startValue, endValue, rangeD):
    for x in range(rangeD):
        lastPos = len(list_return)-1-x
        ran = randint(startValue-1, lastPos)
        list_return[ran], list_return[lastPos] = list_return[lastPos], list_return[ran] 
    print("Ziehung", list_return[-rangeD:])
    return list_return[-rangeD:]

def get_statistic(list):
    global list_stat
    for element in list:
        print(element+startValueZ-1)
        list_stat[element+startValueZ-1] = list_stat[element+startValueZ-1] + 1 


endValueZ = 45
startValueZ = 1
rangeZ = 6

list_stat = {}
for item in range(startValueZ, endValueZ+1):
        list_return.append(item)
        list_stat[item] = 0

def main():
    for index in range(0, 1001):
        rand = get_random_six(startValueZ, endValueZ, rangeZ)
        get_statistic(rand)
    print(list_stat)

if __name__ == "__main__":
    main()





