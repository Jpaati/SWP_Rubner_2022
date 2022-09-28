from random import randint

endValueZ = 49
startValueZ = 0
rangeZ = 7

def get_random_six(startValue, endValue, range):
    list_return = []
    counter = 0
    while counter < range:
        ran = randint(startValue, endValue)             #range immer -1 hinten
        if(not ran in list_return):
            list_return.append(ran)
            counter = counter +1
    print(list_return)
    return list_return
    
list_stat = [0] * (endValueZ + 1)

def get_statistic(list):
    for element in list:
        list_stat[element] = list_stat[element] +1


def print_list(list):
    counter = 0
    for element in list:
        print("Zahl" , counter, ":",element)
        counter = counter +1


for index in range(0, 1000):
    rand = get_random_six(startValueZ, endValueZ, rangeZ)
    get_statistic(rand)

print_list(list_stat)


