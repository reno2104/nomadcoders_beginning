## if, else, elif

password_correct = False

if password_correct:
  print("Here is your money")
else:
  print("Wrong password")


winner = 20
if winner > 10:
  print("winner is greater than 10")
elif winner < 10:
  print("winner is less than 10")
else:
  print("winner is 10")
  
  #---------------------------------------
  
  #age = input("How old r u?")
# input함수는 오직 하나의 argurement만 받는다. 
#print = "user answer", age
# print(type(age))
# 여기서는 age값의 데이터 타입을 나타내준다.

age = int(input("How old r u?"))

if age < 18 :
  print(" u can`t drink")
elif age >= 18 and age <= 35:
  print("u drink beer!")
  # and는 if 와 elif, else 값 모두를 비교해준다. and는 양쪽 모두의 값이 ture여야 실행된다.
elif age == 60 or age == 70:
  # or은 둘중 하나만 맞으면 실행.
  print("Birthday party!")
else:
  print("Go ahead!")

#----------------------------------------

  True and True == True
  True and False == False
  False and True == False
  False and False == False
  
True or True == True
True or False == True
False or True == True
False or False == False