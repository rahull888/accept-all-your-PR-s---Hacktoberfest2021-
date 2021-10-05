# This game is named as Chopsticks Game

# INPUT : 
# Here The Input is taken as follows : 
# step 1 : Move  [Either A(for Attack) or S(for Split) )
# step 2 : Combination 
#    case 1(For Attack):
#        <Attack from> (only one space separated) <Attack To>
#    case 2(For Split):
#        <Hand To be Splitted> <Left Hand after Split> <Right Hand after split>
  

class Game:
    def __init__(self):
        self.person1_left = 1
        self.person1_right = 1
        self.person2_left = 1
        self.person2_right = 1    
        self.result = 0     
        self.person2_turn = False

    def is_over(self):
        
        if self.person1_left == 0 and self.person1_right == 0:
            self.result = 2
            return True
        elif self.person2_left == 0 and self.person2_right == 0:
            self.result = 1
            return True
        else:
            return False

    def current_status(self):         
        print ("Current Status:")
        print("Player1 - ",self.person1_left," ",self.person1_right)
        print("Player2 - ",self.person2_left," ",self.person2_right)
        print("\n") 

    def Attack(self,player,move_from,move_to):
        self.player = player
        self.move_from = move_from
        self.move_to = move_to

        if self.player == 1:
            # player 1 attack from left hand
            if self.move_from == 'L':
                if self.move_to == 'R':
                    self.person2_right += self.person1_left 
                    if self.person2_right >= 5:
                        self.person2_right = 0
                else:
                    self.person2_left += self.person1_left
                    if self.person2_left >= 5:
                        self.person2_left = 0
            
            # Player 1 attack from right hand
            else:
                if self.move_to == 'R':
                    self.person2_right += self.person1_right
                    if self.person2_right >= 5:
                        self.person2_right = 0
                else:
                    self.person2_left += self.person1_right
                    if self.person2_left >= 5:
                        self.person2_left = 0
            

        else:

            # Player 2 attack from left hand
            if self.move_from == 'L':
                if self.move_to == 'R':
                    self.person1_right += self.person2_left 
                    if self.person1_right >= 5:
                        self.person1_right = 0
                else:
                    self.person1_left += self.person2_left
                    if self.person1_left >= 5:
                        self.person1_left = 0


            # Player 2 attack from right hand
            else:
                if self.move_to == 'R':
                    self.person1_right += self.person2_right
                    # If right hand is finger becomes 5 then turn it to 0
                    if self.person1_right >= 5:
                        self.person1_right = 0
                else:
                    self.person1_left += self.person2_right
                    # If left hand finger 5 then turn it to 0
                    if self.person1_left >= 5:
                        self.person1_left = 0


    def splitted(self,player,hand_split,left_split,right_split):
        self.player = player
        self.hand_split = hand_split
        self.left_split = left_split
        self.right_split = right_split
        
        # If player1 split his hand
        if self.player == 1: 
            # If player1 split his left hand
            if self.hand_split == 'L':
                self.person1_right =  self.right_split
                self.person1_left = self.left_split
            else:
                self.person1_right =  self.right_split
                self.person1_left =  self.left_split
        
        # If player 2 split his hand
        else:
            # If player 2 split his Left hand
            if self.hand_split == 'L':
                self.person2_right =  self.right_split
                self.person2_left =  self.left_split
            else:
                self.person2_right =   self.right_split
                self.person2_left =  self.left_split        

                   

game = Game() 
print("\nLet's Start The Game......\n")
game.current_status()

while not game.is_over():       
    
    # Player 2 Turn
    if game.person2_turn:         
        print("Enter move for player 2:")
        move = input()
        player = 2 
        if move == 'A':       
               
           print("Enter the move combination : ")
           n=0 
           combination = input()
           moves = combination.split(" ")

           # Attack Side
           game.Attack(player,moves[0],moves[1])
           game.current_status()
           
        else:
            combination = ['','','']
            print("Enter the move combination - ")
            n=0 
            combination = input()
            moves = combination.split(" ")

            # Spliting side
            game.splitted(player,moves[0],int(moves[1]),int(moves[2]))

            game.current_status()
        game.person2_turn = False
    
    # Player 2 Turn
    else:
        print("Enter move for player 1:")
        move = input()
        player = 1
        if move == 'A':           
           print("Enter the move combination : ")
           n=0 
           combination = input()
           moves = combination.split(" ")

           # Attack Side
           game.Attack(player,moves[0],moves[1])
           game.current_status()
        else:
            combination = ['','','']
            print("Enter the move combination - ")
            n=0 
            combination = input()
            moves = combination.split(" ")

            # Spliting side
            game.splitted(player,moves[0],int(moves[1]),int(moves[2]))
            game.current_status()
        game.person2_turn = True

# Final result of game
if game.result == 1:
    print("Winner of The game is Player 1\n")
elif game.result == 2:
    print("Winner of The game is Player 2\n")             

 