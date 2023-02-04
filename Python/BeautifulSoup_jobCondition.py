from requests import get
from bs4 import BeautifulSoup
# BeautifulSoup: document에서 HTML 태그를 찾게 해주는 모듈
# soup = BeautifulSoup(html_doc, "html.parser")
# soup.find_all("")

base_url = "https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?occupation=&notSrcKeyword=&_csrf=b1cc193a-2d14-4cc8-b434-bea01f1a582c&region=&srcKeyword="
search_srcKeyword = "python"

response = get(f"{base_url}{search_srcKeyword}")
if response.status_code != 200:
  print("Can`t request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  list = soup.find_all('td', class_="a-l va-t")
  #  print(len(list))  : 집계된 코드의 갯수
  #  print(response.text)
  # .text : 웹사이트를 구성하고 있는 코드

  for cop_name in list:
    cpName = cop_name.find_all(class_='cp_name')
    condition = cop_name.find_all('em')
    sallary = cop_name.find_all(class_='cp-info')

    #sallary.pop(1)
    # 원하는 항목 지우기

    print("///////////")
    print(cpName, condition, sallary)
    """ #각 항목마다 구분하기 위한 코드인데, 워크넷사이트는 이거 안써도 구별이 되어있다.
    for cpname in cpName:
      print(cpname)
      print("/////////////")
    """
"""

P.s.
1. Last time, I searched only by company name, but this time I listed it by company name, condition, and salary.
2. in the salary, There are a lot of empty spaces;;;
