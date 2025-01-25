import random
action_list = ['rock', 'paper', 'scissor']

computer_score = 0
player_score = 0
total_rounds = input("How many rounds do you want to play?")
round_counter = 0

while True:
    round_counter +=1
    print('Round number:', round_counter)
  
    computer_choice = random.choice(action_list)
    player_choice = input("What is your action?")
  
    print("Computer's choice:", computer_choice)
    print("Player's choice:", player_choice)
  
    if computer_choice == player_choice:
       print("Tie")
    
    elif computer_choice =='paper':
       if player_choice == 'rock':
           print('Computer wins')
           computer_score +=1
       else:
           print('Player wins')
           player_score +=1

    elif computer_choice == 'rock':
       if player_choice == 'paper':
           print('Player wins')
           player_score +=1
       else:
           print('Computer wins')
           computer_score +=1

    else:
       if player_choice =='rock':
           print('Player wins')
           player_score +=1
       else:
           print('Computer wins')
           computer_score +=1
      
    if round_counter == int(total_rounds):
        break

if computer_score == player_score:
  print('There is no winner.Tie!')
elif computer_score > player_score:
  print('Computer wins the game.')
else:
  print('Player wins the game.')