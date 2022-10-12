from logging import Filter
import random
from random import randint
from xml.dom.minidom import Element

list_PokerCards = []

list_Type = ["Kreuz", "Pik", "Herz", "Karo"]    #Arten von Karten
list_number = [2,3,4,5,6,7,8,9,10, 'Jack', 'Queen', 'King', 'Ace']

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
    print("Ziehung:", poker_Cards[-5:])
    return poker_Cards[-5:]

def check_Poker_Pair(random_Five):
    for number in list_number:
        ele = len(list(filter(lambda pCard : pCard['number'] == number, random_Five))) # get len of number, if double is there
        if(ele == 2):
            return True
    return False

def check_Poker_Three(random_Five):
    for number in list_number:
        ele = len(list(filter(lambda pCard : pCard['number'] == number, random_Five))) # get len of number, if double is there
        if(ele == 3):
           return True
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
    for number in list_number:
        ele = len(list(filter(lambda pCard : pCard['number'] == number, random_Five))) # get len of number, if double is there
        if(ele == 4):
           return True
    return False

def check_Royal_Street(random_Five):
    list_index = []
    for item in random_Five:
        list_index.append(list_number.index(item['number']))
    list_index.sort()
    if(check_Straight(list_index) and list_index[0] == 8):
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

#TODO: Auswertung erstellen

define_Cards()

for i in range(0, 100000):
    list_random_Five = get_random_5(list_PokerCards)
    isPair = check_Poker_Pair(list_random_Five)
    isThree = check_Poker_Three(list_random_Five)
    isFlush = check_Flush(list_random_Five)
    isStraight = check_Street(list_random_Five)
    isFullHouse = check_Full_House(list_random_Five)
    isFour = check_Four(list_random_Five)
    isRoyalStreet = check_Royal_Street(list_random_Five)
    isRoyalStreetFlush = check_Royal_Street_Flush(list_random_Five)
    print("ID: ", i, isPair, isThree, isFlush, isStraight, isRoyalStreet, isRoyalStreetFlush)
    if(isRoyalStreetFlush): exit()
