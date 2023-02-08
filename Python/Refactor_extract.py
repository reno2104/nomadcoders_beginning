from requests import get  
from bs4 import BeautifulSoup  
# 기존 BeautifulSoup로 만든 잡스크래퍼를 다른 곳으로 옮기고, 기존 .py에 연동을 시켜 실행되게 하기.
# 이것이 객체지향인가...
from extractors.wwr import extract_wwr_jobs

jobs = extract_wwr_jobs("python")
print(jobs)
