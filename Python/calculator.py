#  +, - , * , / , ** 연산자를 사용하여 계산기 만들기


# 1. 🍗
def plus(a=0, b=0):
    print(a, "+", b,"=", a+b)

def minus(a=0, b=0):
    print(a - b)

def dev(a=0, b=0):
    if (b==0):
        print("0으로 나눌 수 없습니다.")
    else:
        print(a, "/", b, "=",a/b)

def multip(a=0, b=0):
    print(a * b)


    #2. 🍠
def cal(a, b):
    print(a, "(?)", b)
    print("--------")
    print("(+) :", a + b)
    print("(-) :", a - b)
    print("(/) :", a / b)
    print("(*) :", a * b)
    print("(**) :", a ** b)

cal(3, 3)


#3. 🌯
Warning = "Hmmmmm, nothing to calculate. Try again with number and sign [plus => +, minus => -, divide=> /, multiple => *, square=> **] ex) a, \"+\" , b "
def calc(a=Warning, how=Warning, b=Warning):

#기호가 무엇인지 파악
    if how == "":
        print(Warning)

    elif how == "+":
        print(a + b)

    elif how == "-":
        print(a - b)

    elif how == "*":
        print(a * b)

    elif how == "**":
        print(a**b)

# 아무런 기호가 없거나 위에 상황이 아닐때
    else:
        print(Warning)

calc(1, "+", 2)


# 4.  🥠
def plus(a=0,b=0):
    print("plus(",a,"+",b,")=",a+b)
def ma(a=0,b=0):
    print("ma(",a,"-",b,")=",a-b)
def gub(a=0,b=1):
    print("gub(",a,"*",b,")=",a*b)
def na(a=0,b=1):
    print("na(",a,"/",b,")=",a/b)
def je(a=0):
    print("je(",a,")=",a*a)

plus()
plus(1)
ma()
ma(1)
gub()
gub(3)
na()
na(3)
je()
je(3)