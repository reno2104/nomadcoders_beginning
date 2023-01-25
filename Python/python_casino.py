***
from random import randint

print("Welcome to Python Casino!")
pc_choice = randint(1, 50)

playing = True

while playing:
          user_choice = int(input("Choose number(1~50): "))
          if user_choice == pc_choice:
            print("u win!")
            playing = False
          elif user_choice > pc_choice:
            print("Lower!")
          elif user_choice < pc_choice:
            print("Higher! ")

***


from random import randint
print("Welcome to Python Casino")
print("You have 10 chances")

pc_choice = randint(1, 50)

playing = True
chance = 10

while playing:
  chance = chance - 1
if chance >= 0:
  user_choice = int(input("Choose number."))
if user_choice == pc_choice:
  print("You won!")
  playing = False
elif user_choice > pc_choice:
  print("Lower!")
  print("You have", chance, "chances")
elif user_choice < pc_choice:
  print("Higher!")
  print("You have", chance, "chances")
elif chance < 0:
  print("Game over")
  playing = False