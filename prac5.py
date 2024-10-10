print("welcome to python pizza delivery!")
size=input("What size of pizza do you want? S,M,L? ")
peperroni=input("Do you want peperromi on your pizza? Y or N? ")
cheese=input("Do you want extra chees? Y or N? ")
bill=0
if size=="S":
  bill=15
if size=="M":
  bill=20
if size=="L":
  bill=25

if peperroni=="Y":
  if size=="S":
    bill+=2
  else:
    bill+=3

if cheese== "Y":
  bill+=1
print(f"Your final bill is {bill}")   