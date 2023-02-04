def say_hello(name,age):
  print(F"Hello {name} u r {age} years old.")

say_hello("reno", 13)
#positional argument 는 자리를 신경써야 한다.

say_hello(age=13, name="reno")
# Keyward argument : argument의 이름을 넣어주면 더이상 순서는 신경쓰지 않아도 된다.
