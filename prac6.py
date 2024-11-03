print('''
                  _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to treasure island!")
print("Your mission is to find a treasure")
choice=input("There's a crossroad. Move left or right? ").lower()
if choice=="left":
  print("You met a bridge.")
  water=input("Swim or Climb bridge? ").lower()
  if water=="climb bridge":
    door=input("Choose a door. Iron or Wooden? ").lower()
    if door=="wooden":
      print("You found three boxes, one contains the treasure.")
      color=input("Choose a color of box. Yellow, black or gold? ").lower()
      if color=="black":
        print("You found the Treasure. Winner!!!")
      elif color=="gold":
        print("The box swallowed you.Game Over!!!")
      else:
        print("Empty box.Game Over!!!")
    else:
      print("You fought a Lion and died.Game Over!!!")
  else:
    print("You got bitten by a crocodile!.Game Over!!!")
else:
  print("The road is blocked.Game Over!!!")