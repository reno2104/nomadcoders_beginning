from requests import get

websites = (
  "google.com", 
  "naver.com",   
  "https://nate.com", 
  "daum.net",
  "https://youtube.com"
)

results = {
  
}

for website in websites:
  if not website.startswith("https://"):

    website = f"https://{website}"
response = get(website)
# print(response.status_code)
#웹사이트가 성공적으로 응답하는지 알수있는 코드.
if response.status_code == 200:
  # print(f"{website} is ok")
  results[website] = "Ok"
else: 
 # print(f"{website} is not ok")
  results[website] = "Failed"
  print(results)
