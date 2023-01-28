# 1. 파이썬한테 tuple안에 있는 각각의 item을 사용해서 코드를 실행하는 법. (반복문)

websites = (
  "google.com",
  "naver.com",
  "nate.com",
  "daum.net",
  "youtube.com"
)

#리스트가 얼마나 긴지 신경을 쓰지않고, 각 item을 활용해서 파이썬이 자동으로 코드를 실행하라고 할 방법 찾기

for each in websites:
  print("each is equals to",each)
# tuple외에 list도 가능.

# 2. 현재 처리중 item이 무엇인지 알 수 있게 하기

#for문은 각각의 item이 실행될 때 placeholder를 만드는 것을 허락한다.
