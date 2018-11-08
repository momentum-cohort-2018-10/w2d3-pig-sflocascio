#PIG
import random

class Die:
    def __init__(self):
        self.value = random.choice([1, 2, 3, 4, 5, 6])
    def roll(self):
        random.choice(self.value)
    def __str__(self):
        print(f"Rolled a {self.value}")
        return(f"Rolled a {self.value}")

dice = Die()
print(dice)
        
class Temporary_score:
    def __init__(self):
        self.value = 0
    def reset_temporary_score(self):
        self.value = 0
    def add_dice_value(self, dice_value):
        self.value = self.value + dice_value
    def __str__(self:
        return (f"Your temporary roll score is {self.value}")

class Computer_player:
    def __init__(self):
    
    def roll_until_twenty(temporary_score):
        while temporary_score < 20:
            print("computer rolls again")
            return roll_the_dice()
        else:
            print ("computer holds")
            return new_turn()    

class Human_player:
    def __init__(self):
        def human_decision():
            make_decision = int(input("Press 1 to roll again or 2 to hold"))
            if make_decision == 1:
                return roll_the_dice()
            else:
                return new_turn ()

class Scoreboard:
    def __init__(self, human, computer, temporary_score):
        self.human = human
        self.computer = computer
        self.temporary_score = temporary_score
    def__str__(self):
    return (f"Current Game Score, human = {self.human}, computer = {self.computer}")

 def check_score_for_win(self):
        if self.human.player.score >= 100:
            print("Human_player wins!")
        elif self.computer.player.score >= 100:
            print("Computer_player Win")

def assign_score(self):
    #this needs to assign the roll to the temporary roll class 

def choose_first_player(self):
    #this function chooses randomly if the computer of human goes first

class Game: 
    def __init__(self):
        self.computer_player = Computer_Player()
        self.human_player = Human_player()
        self.die = Die()
        self.temporary_score = Temporary_score()
        self.score = Score(self.human_player, self.computer_player)

    def start_game(self):
        while self.human_player.score < 100 and self.computer_player < 100:
            self.play_game()
        
    def play_game(self):
        if type(Human_player):
            roll_the_dice()
            self.temporary_score.reset_temporary_score()
            print(self.score)
            if self.dice != 1
                return new_turn
            else:
                self.human_player.human_decision
        if type(Computer_player)
            roll_the_dice()
            self.temporary_score.reset_temporary_score()
            print(self.score)
            if self.dice != 1
                return new_turn
            else:
                self.computer_player.computer_decision






   

    




    

#     #Functions to use:

#     def ask_player_if_hold():

#     def roll_again(): 

#     def player_turn():
        # this function takes a given player,  gives them a roll and displays it..
        # Uses a while statement to determine that players roll is not value of 1
        #   if players value is 1, display score + return back to next player turn
        #   if players value is not 1, display turn score and total score, and prompt to hold or hit 
        # if hold: tallys score and goes to next round 
        # if hit: uses roll_again function to initialize another roll and adds it to turn total 
        # continues until player holds, rolls 1, or hits 100

    # def computer_turn():
        # this function takes a computer player,  gives them a roll and displays it..
        # Uses a while statement to determine that players roll is not value of 1
        #   if players value is 1, display score + return back to next player turn
        #   if players value is not 1, and turns score is < 20, computer will hit 
        # if hold: tallys score and goes to next round 
        # if hit: uses roll_again function to initialize another roll and adds it to turn total 
        # continues until player holds, rolls 1, or hits 100






































# if __name__ == "__main__":
#     game = Game()
#     game.play_round()