from requests import get
from bs4 import BeautifulSoup
# BeautifulSoup: document에서 HTML 태그를 찾게 해주는 모듈
# soup = BeautifulSoup(html_doc, "html.parser")
# soup.find_all("")

base_url ="https://www.work.go.kr/wnSearch/unifSrch.do?topQuery="
search_topQuery="python"

response = get(f"{base_url}{search_topQuery}")
if response.status_code != 200:
  print("Can`t request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
 job = soup.find_all("strong", class_="highlight")
   print(response.text)
# .text : 웹사이트를 구성하고 있는 코드
