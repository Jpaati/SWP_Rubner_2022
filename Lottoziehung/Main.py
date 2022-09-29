from random import randint

def get_random_six(startValue, endValue, rangeD):
    list_return = []
    for item in range(startValue, endValue+1):
        list_return.append(item)
        list_stat[item] = 0

    for x in range(rangeD):
        lastPos = len(list_return)-1-x
        ran = randint(startValue, endValue-1)
        list_return[ran], list_return[lastPos] = list_return[lastPos], list_return[ran] 
    print("Ziehung", list_return[:-rangeD])
    #TODO: correct ERROR
    return list_return[:-rangeD]

def get_statistic(list):
    for element in list:
        list_stat[element+startValueZ-1] = list_stat[element+startValueZ-1] +1


def print_list(list):
    counter = 0
    for element in list:
        print("Zahl" , counter, ":",element)
        counter = counter +1

endValueZ = 45
startValueZ = 1
rangeZ = 6

list_stat = {}

for index in range(0, 1001):
    rand = get_random_six(startValueZ, endValueZ, rangeZ)
    get_statistic(rand)
    #Statistik not right
print_list(list_stat)





