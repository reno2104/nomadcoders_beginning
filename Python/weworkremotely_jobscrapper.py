# 1.요청
# 2.응답
# 3.응답 파싱
# 4.데이터를 원하는대로 만지기

# 다운로드한 library 포함
from requests import get  # http 요청을 위해 lib
from bs4 import BeautifulSoup  # 응답 결과를 파싱 하여 가공 하기 위한 lib

# 요청 사이트 url
base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

# 요청후 응답 받기
response = get(f"{base_url}{search_term}")
# 포트가 200이 아니라면,
if response.status_code != 200:
  print("Can't request website")

else:
  # 결과에서 원하는 데이터 추출
  results = []
  # html을 파싱하여 결과 받기
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_="jobs")
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop()  # 마지막 요소 제거, -1 기재해도 같은 결과
    for post in job_posts:
     anchors = post.find_all('a')
     anchor = anchors[1]
     link = anchor['href']
      
     company, kind, region = anchor.find_all('span', class_=("company"))
     title = anchor.find('span', class_=("title"))
     data_result = {
        'link' : f"https://weworkremotely.com{link}",
        #'title': title.string,
        'company': company.string,
        'kind': kind.string,
        'region': region.string
}
results.append(data_result)
# print(company,kind,region,title)
# link = anker['href'] # dicts 처럼 태그의 요소를 가져올 수 있다.
# print(link)

for result in results:
  print(result)
  print("//////////////////////////")
  print("//////////////////////////")
