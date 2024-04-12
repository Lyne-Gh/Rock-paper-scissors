import random

Options =['rock', 'paper', 'scissors']

draws =0
wins=0
compWins=0

while True:
    user_answer = input( "Type Rock/Paper/scissors if you want to play or Q to quit the game: ").lower()
    if user_answer== "q":
        print("See you next time")
        break
    if user_answer not in Options:
        continue

    r= random.randrange(3)
    computer_choice = Options[r]
        
    if (user_answer == 'rock' and computer_choice == Options [1]):
        print ('You chose '+ user_answer +' the computer chose '+ computer_choice + ' Computer wins!')
        compWins +=1
        continue
        
    
    elif (user_answer == 'rock' and computer_choice == Options [2]):
        print ('You chose '+ user_answer +' the computer chose '+ computer_choice + ' You win!')
        wins += 1
        continue
             
    elif (user_answer == 'rock' and computer_choice == Options [0]):
        print ('You chose '+ user_answer +' the computer chose '+ computer_choice + ' It\'s a draw!')
        draws +=1
        continue   

    elif (user_answer == 'paper' and computer_choice == Options [1]):
        print ('You chose '+ user_answer +' the computer chose '+ computer_choice + ' It\'s a draw!')
        draws +=1
        continue

    elif (user_answer == 'paper' and computer_choice == Options [2]):
        print ('You chose '+ user_answer +' the computer chose '+ computer_choice + ' Computer wins!')
        compWins +=1
        continue

    elif (user_answer == 'paper' and computer_choice == Options [0]):
        print ('You chose '+ user_answer +' the computer chose '+ computer_choice + ' You win!')
        wins += 1
        continue
        

    elif (user_answer == 'scissors' and computer_choice == Options [1]):
        print ('You chose '+ user_answer +' the computer chose '+ computer_choice + ' You win!')
        wins += 1
        continue

    elif (user_answer == 'scissors' and computer_choice == Options [2]):
        print ('You chose '+ user_answer +' the computer chose '+ computer_choice + ' It\'s a draw!')
        draws +=1
        continue

    elif (user_answer == 'scissors' and computer_choice == Options [0]):
        print ('You chose '+ user_answer +' the computer chose '+ computer_choice + ' Computer wins!')
        compWins +=1 
        continue

print (" I hope you enjoyed the game you won : " + str (wins)+ " times!")       
print (" Computer won : " + str (compWins)+ " times!")    
print (" And it was a draw : " + str (draws)+ " times!")   

