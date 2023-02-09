from requests import get  # http 요청을 위해 lib
from bs4 import BeautifulSoup  # 응답 결과를 파싱 하여 가공 하기 위한 lib
from extractors.wwr import extract_wwr_jobs

# jobs = extract_wwr_jobs("python")
# print(jobs)

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Cant request page.")
else :
  soup = BeautifulSoup(response.text, "html.parser")
  job_list = soup.find("ul", class_="jobsearch-ResultsList")
  jobs = job_list.find_all('li', recursive=False)
  # print(len(jobs))
  # ul안에서 모든 li들 갯수. 특히 최상단 ul의 li말고도 다단계식의 li도 전부 찾아낸다. 
  # 때문에, BeautifulSoup에게 바로 아래에 있는 것만 검색해달라고 요청하려면... 찾고자 하는 find_all() 옆에 recursive=False를 붙여야 하는 것이다.
  for job in jobs:
    print(job)
    print("///////")
