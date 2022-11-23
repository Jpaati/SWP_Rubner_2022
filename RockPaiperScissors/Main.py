import random

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
        print("Player1:", self.score_Player1, "Player2:" , self.score_Player2)
        print("Chosen Symbols:" , self.chosen_symbols)
    
def generate_Player_Hand(figureStr):
    if(figureStr == 'Rock'):
        return Hand('Rock', ['Spock', 'Paper'])
    elif(figureStr == 'Paper'):
        return Hand('Paper', ['Scissor', 'Lizard'])
    elif(figureStr == 'Scissor'):
        return Hand('Scissor', ['Rock', 'Spock'])
    elif(figureStr == 'Lizard'):
        return Hand('Lizard', ['Rock', 'Scissor'])
    elif(figureStr == 'Spock'):
        return Hand('Spock', ['Lizard', 'Paper'])
    return "Wrong Input"

        
if __name__ == "__main__":
    hand_list = [Hand("Rock", ['Spock', 'Paper']), Hand('Paper', ['Scissor', 'Lizard']), Hand('Scissor', ['Rock', 'Spock']), Hand('Lizard', ['Rock', 'Scissor']), Hand('Spock', ['Lizard', 'Paper'])]
    game1 = Game(hand_list)

    while game1.round_counter < 3:
        comp = random.choice(hand_list)
        print()
        print("Insert your Hand: [Rock, Paper, Scissor, Lizard, Spock]")
        playerHand = generate_Player_Hand(input())
        
        game1.play_a_round(playerHand, comp)
        print("opponent:", comp.figure)
    game1.print_score()