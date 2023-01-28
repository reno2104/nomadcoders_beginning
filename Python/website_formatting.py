websites = ("google.com", "naver.com", "https://nate.com", "daum.net",
            "https://youtube.com")

# website가 https://로 시작하지않을 때 처리하는 중요한 부분
for website in websites:
  if not website.startswith("https://"):
    #string 안에 변수 넣는 방법
    website = f"https://{website}"
  #if문 밖에 있는 print 출력
  print(website)
