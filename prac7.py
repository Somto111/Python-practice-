rock='''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       '''
paper='''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' 
'''
scissors='''
_      ___ _______
|  _,-' _ `\______)
|~'    ' `\()
|       (____)
|      (_____)
|--.____(___)'''


game_images=[rock, paper, scissors]
users_choice =int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
print(game_images[users_choice])
import random
computers_choice=random.randint(0,2)
print("computer chose:")
print(game_images[computers_choice])
if users_choice >= 3:
  print("You entered an invalid nmber. You lose!")
elif users_choice==0 and computers_choice==1:
  print("You win!")
elif computers_choice==users_choice:
  print("It is a draw!")
elif computers_choice==0 and users_choice==2:
  print("You win!")
elif users_choice==0 and computers_choice==2:
  print("You win!")
elif computers_choice > users_choice:
  print("You lose!")
elif users_choice > computers_choice:
  print("You win!")