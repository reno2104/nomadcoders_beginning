from random import randint
#random.randint(a,b) : 첫번째 파라미터 a는 N보다 작거나 같고, N은 두번째 파라미터 b보다 작거나 같다.

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

# import없이 모듈종류 알아보는 방법  https://docs.python.org/3/library/functions.html