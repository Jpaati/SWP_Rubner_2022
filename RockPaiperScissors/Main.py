import random
import requests

gotDataFromServer = False

class Hand:
    def __init__(self, figure, is_beaten_by):
        self.figure = figure
        self.is_beaten_by = is_beaten_by
    
    def can_beat(self, figure2):
        return self.figure in figure2.is_beaten_by


class Game:
    def __init__(self, hand):
        self.score_Player1 = 0
        self.score_Player2 = 0
        self.round_counter = 0
        self.chosen_symbols = {}
        self.player_won = False
        for item in hand:
            self.chosen_symbols[item.figure] = 0

    def play_a_round(self, player1, player2):
        if(playerHand == 'Wrong Input'):
            print("Falsche Hand")
            return ""
        if(player1.can_beat(player2)):
           self.score_Player1 +=1
           print("You Won")
        elif(player2.can_beat(player1)):
            self.score_Player2 += 1
            print("Computer won")
        else:
            print("Tie")
        self.round_counter += 1
        self.chosen_symbols[player1.figure] +=1
        self.chosen_symbols[player2.figure] +=1

    def print_score(self):
        if(self.score_Player1 < self.score_Player2):
            self.player_won = True
        print("Player1:", self.score_Player1, "Player2:" , self.score_Player2)
        print("Chosen Symbols:" , self.chosen_symbols)
    
def generate_Player_Hand(figureStr):
    if(figureStr == 'Rock'):
        return Hand("Rock", ['Spock', 'Paper'])
    elif(figureStr == 'Paper'):
        return Hand("Paper", ['Scissor', 'Lizard'])
    elif(figureStr == 'Scissor'):
        return Hand("Scissor", ['Rock', 'Spock'])
    elif(figureStr == 'Lizard'):
        return Hand("Lizard", ['Rock', 'Scissor'])
    elif(figureStr == 'Spock'):
        return Hand("Spock", ['Lizard', 'Paper'])
    return "Wrong Input"

def data_to_Server(chosen_symbols, player_Name, player_won):
    j = {'player_name': player_Name, 'chosen_symbols': chosen_symbols, 'player_won': player_won}
    response = requests.put('http://localhost:5000/data/0' , json=j)
    print(response)

def get_Data_from_Server(player_Name):
    response = requests.get('http://localhost:5000/search/'+ player_Name)
    get_Data_For_Algorithm(response.json())
    global gotDataFromServer
    gotDataFromServer = True
    return response

dic_stats = {"Rock": 0, "Paper" : 0, "Scissor": 0, "Lizard": 0, "Spock": 0}

def get_Data_For_Algorithm(data):
    for item in data:
        string = str(item['chosen_symbols'])
        string = string[1:-1]
        js_ar = string.split(",")
        for ele in js_ar:
            arr = ele.split(":")
            arr[0] = arr[0].replace(" ", "")
            arr[0] = arr[0][1:-1]
            dic_stats[arr[0]] += int(arr[1])
    print(dic_stats)
    return dic_stats

def get_computer_hand(listd):
    if(gotDataFromServer):
        sumd = sum(dic_stats.values())
        print(dic_stats.values())
        for ele in dic_stats:
            dic_stats[ele] = dic_stats[ele] / sumd
        print(dic_stats)
        symbol_max = max(dic_stats, key=dic_stats.get)
        dic_stats.pop(symbol_max)
        return generate_Player_Hand(symbol_max)
    else:
        return random.choice(listd)


if __name__ == "__main__":
    hand_list = [Hand("Rock", ["Spock", "Paper"]), Hand("Paper", ["Scissor", "Lizard"]), Hand("Scissor", ["Rock", "Spock"]), Hand("Lizard", ["Rock", "Scissor"]), Hand("Spock", ["Lizard", "Paper"])]
    ongoing = True
    print("INSERT your name:")
    player_name = input()

    while(ongoing):
        print("Your options", player_name, ": Stats[0], Play[1], CompVSComp[2]")
        choice = input()

        if(int(choice) == 0):
            data = get_Data_from_Server(player_name)
            print(data.json())

        elif(int(choice) == 1):
            print("Hallo")
            game1 = Game(hand_list)

            while game1.round_counter < 3:
                comp = get_computer_hand(hand_list)
                print()
                print("Insert your Hand: [Rock, Paper, Scissor, Lizard, Spock]")
                playerHand = generate_Player_Hand(input())
        
                game1.play_a_round(playerHand, comp)
                print("opponent:", comp.figure)
            game1.print_score()

            print("Want to continue?: Yes[0] No[1]")
            game1.round_counter = 0
            ongoingD = input()
            if(ongoingD == 0):
                ongoing = True
            if(ongoingD == 1):
                ongoing = False
            
            data_to_Server(str(game1.chosen_symbols), player_name, game1.player_won)
        
        elif int(choice) == 2:
            print("GameMode: Computer (Data) vs. Computer (Random)")
            print("Insert Name for Data:")
            player_1 = input()
            
            response1 = get_Data_from_Server(player_1)
            print("Player1", response1.json())
            hand_player1 = get_computer_hand(hand_list)
            print("Hand_Player1", hand_player1)

            game2 = Game(hand_list)
            while game2.round_counter < 3:
                comp = get_computer_hand(hand_list)
                playerHand = random.choice(hand_list)
        
                game2.play_a_round(playerHand, comp)
                print("opponent:", comp.figure)
            print("YOUR STATS")
            game2.print_score()

