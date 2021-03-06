# import rock_paper_scissors.py as helpers
import random

class Game:

    def __init__(self):
        "Keep count of all games played and their results"
        self.wins=int(0)
        self.losses=int(0)
        self.draws=int(0)

    def get_user_item(self):
        flag=True
        while(flag):
            entered=input("Please choose Rock, Paper, or Scissors: ")
            if(entered.lower()=='rock'):
                return 'rock'
            elif(entered.lower()=='paper'):
                return 'paper'
            elif(entered.lower()=='scissors'):
                return 'scissors'

    def get_computer_item(self):
        rand=random.randint(0,2)
        if(rand==0):
            return 'rock'
        elif(rand==1):
            return 'paper'
        elif(rand==2):
            return 'scissors'

    def get_game_result(self, user_item, computer_item):
        #user entered rock
        if(user_item=='rock'):
            if(computer_item=='rock'):
                self.draws+=1
                return 'draw'
            elif(computer_item=='paper'):
                self.losses+=1
                return 'loss'
            elif(computer_item=='scissors'):
                self.wins+=1
                return 'win'
        #user entered paper
        elif(user_item=='paper'):
            if(computer_item=='rock'):
                self.wins+=1
                return 'win'
            elif(computer_item=='paper'):
                self.draws+=1
                return 'draw'
            elif(computer_item=='scissors'):
                self.losses+=1
                return 'loss'
        #user entered scissors
        elif(user_item=='scissors'):
            if(computer_item=='rock'):
                self.draws+=1
                return 'draw'
            elif(computer_item=='paper'):
                self.losses+=1
                return 'loss'
            elif(computer_item=='scissors'):
                self.wins+=1
                return 'win'


def play():
    newGame=Game()
    user_input=newGame.get_user_item()
    comp_input=newGame.get_computer_item()
    result=newGame.get_game_result(user_input,comp_input)
    if(result=='win'):
        temp='won!'
    elif(result=="loss"):
        temp='lose.'
    elif(result=='draw'):
        temp='drew!'
    print(f'You selected {user_input}. The Computer selected {comp_input}. You {temp}')
    
    return result



# play()

