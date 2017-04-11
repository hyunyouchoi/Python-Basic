tie=0    
player1win =0
player2win =0

def rps(player1, player2):
    if player1 == 'r' and player2 == 'r':
        return 0
    elif player1 == 'p' and player2 == 'p':
        return 0
    elif player1 == 's' and player2 == 's':        
        return 0      
    elif player1 == 'r' and player2 == 'p':        
        return 1       
    elif player1 == 'r' and player2 == 's':        
        return -1       
    elif player1 == 'p' and player2 == 's':        
        return 1
    elif player1== 's' and player2 == 'r':        
        return 1       
    elif player1 == 's' and player2 == 'p':        
        return -1       
    elif player1 == 'p' and player2 == 'r':
        return -1       

def display(rpsreuslt):
    if result == 0:
      
       tie += 1
       print ("There were ",tie,"ties.")
    elif result == -1:
       
       player1win += 1
       print ("player 1 won ",player1win,"times.")
    elif result == 1:
       
       player2win += 1
       print ("player 2 won ",player2win,"times.")
       


playagain = 'y'
while playagain == 'y':
      p1 = input("Player1: Please select rock(r), paper(p), or scissors(s): ")
      p2 = input("Player2: Please select rock(r), paper(p), or scissors(s): ")
      result = rps(p1,p2)
      
      if result == 0:         
         tie += 1
         
      elif result == -1:           
           player1win += 1
            
      elif result == 1:           
           player2win += 1

      playagain = input('Play again? Enter y for yes or n for no: ')
           
print("****** Final Results ******\n"
      "player 1 won ",player1win,"times.\n"
      "player 2 won ",player2win,"times.\n"
      "There were ",tie,"ties.")
      




           
           
           
      




   
    
