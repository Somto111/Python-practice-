print("Welcome to rollercoaster ride!")
height=int(input("what's your height in cm? "))
if height>=120:
  age=int(input("what is your age? "))
  if age<=12:
    bill=5
    print("Child ticket is $5")
  elif age<=18:
    bill=7
    print("Youth ticket is $7")
  else:
    bill=12
    print("Adult ticket is $12")
  
  photo=str(input("do you want your photo taken? if yes type y and n for no " ))
  if photo=="y":
    bill += 3
    print(f"Your final bill is {bill}")
    
else:
  print("Sorry you need to grow taller")