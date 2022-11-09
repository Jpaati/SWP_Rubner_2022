import random
from random import randint
from xml.dom.minidom import Element

list_PokerCards = []

list_Type = ["Kreuz", "Pik", "Herz", "Karo"]    #Arten von Karten
list_number = [2,3,4,5,6,7,8,9,10, 'Jack', 'Queen', 'King', 'Ace']
list_possible_outcomes = ["Royal Street Flush", "Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind", "Two Pairs", "One Pair", "High Card"]

dict_stat= {}

def define_dict():
    for item in list_possible_outcomes:
        dict_stat[item] = 0

def filter_methode(random_Five):
    pairCounter = 0
    for number in list_number:
        ele = len(list(filter(lambda pCard : pCard['number'] == number, random_Five))) # get len of number, if double is there
        if(ele == 4):
           return 4
        elif(ele == 3):
            return 3
        elif(ele == 2):
            pairCounter = pairCounter +1
    return pairCounter

def get_Stat(list_Cards):
    if(check_Royal_Street_Flush(list_Cards)):
        dict_stat["Royal Street Flush"] +=1
    elif(check_Straight_Flush(list_Cards)):
        dict_stat["Straight Flush"] +=1
    elif(check_Four(list_Cards)):
        dict_stat["Four of a Kind"] +=1
    elif(check_Full_House(list_Cards)):
        dict_stat["Full House"] +=1
    elif(check_Flush(list_Cards)):
        dict_stat["Flush"] +=1
    elif(check_Street(list_Cards)):
        dict_stat["Straight"] +=1
    elif(check_Poker_Three(list_Cards)):
        dict_stat["Three of a Kind"] +=1
    elif(check_Poker_Pair(list_Cards) == 2):
        dict_stat["Two Pairs"] +=1
    elif(check_Poker_Pair(list_Cards) == 1):
        dict_stat["One Pair"] +=1
    else:
        dict_stat["High Card"] +=1

def define_Cards():
    for typed in list_Type:
        for number in list_number:
            list_PokerCards.append({'type' : typed, 'number': number})
    random.shuffle(list_PokerCards)

def get_random_5(poker_Cards):
    for x in range(5):
        lastPos = len(poker_Cards)-1-x
        ran = randint(0, lastPos)
        poker_Cards[ran], poker_Cards[lastPos] = poker_Cards[lastPos], poker_Cards[ran]
    return poker_Cards[-5:]

def check_Poker_Pair(random_Five):
    if(filter_methode(random_Five) == 1 or filter_methode(random_Five) == 2):
        return filter_methode(random_Five)

def check_Poker_Three(random_Five):
    if(filter_methode(random_Five) == 3):
        return True
    else:
        return False

def check_Flush(random_Five):
    for type in list_Type:
        ele = len(list(filter(lambda pCard : pCard['type'] == type, random_Five))) # get len of number, how often same is there
        if(ele == 5):
            return True
    return False

def check_Full_House(random_Five):
    return check_Poker_Three(random_Five) and check_Poker_Pair(random_Five)

def check_Straight(list_index):
    for i in range(len(list_index)-1):
        if(abs(list_index[i] - list_index[i+1]) != 1 ):
            return False
    return True

def check_Street(random_Five):
    list_index = []
    for item in random_Five:
        list_index.append(list_number.index(item['number']))
    list_index.sort()
    if(check_Straight(list_index)):
        return True
    else:
        return False

def check_Four(random_Five):
    if(filter_methode(random_Five) == 4):
        return True
    else:
        return False

def check_Straight_Flush(random_Five):
    list_index = []
    list_kind = []
    for item in random_Five:
        list_index.append(list_number.index(item['number']))
        list_kind.append(item['type'])
    list_index.sort()
    if(check_Straight(list_index) and list_kind.count(list_kind[0]) == len(list_kind)):
        return True
    else:
        return False

def check_Royal_Street_Flush(random_Five):
    list_index = []
    list_kind = []
    for item in random_Five:
        list_index.append(list_number.index(item['number']))
        list_kind.append(item['type'])
    list_index.sort()
    if(check_Straight(list_index) and list_index[0] == 8 and list_kind.count(list_kind[0]) == len(list_kind)):
        return True
    else:
        return False

sized = 10000

def dict_to_decimal():
    for item in dict_stat:
        dict_stat[item] = round(dict_stat[item]/sized, 2)


if __name__ == "__main__":
    define_Cards()
    define_dict()
    for i in range(0, sized):
        list_random_Five = get_random_5(list_PokerCards)
        get_Stat(list_random_Five)
        print(i)
    dict_to_decimal()
    print(dict_stat)