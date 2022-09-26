from random import randint

def get_random_six():
    list_return = []
    for i in range(0, 6):
        ran = randint(0,45)
        if(not ran in list_return):
            list_return.append(ran)
    return list_return


list_stat = [0] * 46

def get_statistic(list):
    for element in list:
        list_stat[element] = list_stat[element] +1


def print_list(list):
    counter = 0
    for element in list:
        print("Zahl" , counter, ":",element)
        counter = counter +1


for index in range(0, 1000):
    rand = get_random_six()
    get_statistic(rand)

print_list(list_stat)


