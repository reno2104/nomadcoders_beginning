# 크롬을 사용자의 경우, 로컬 또는 최신버전 셀레니움 사용자분들중 브라우저가 자꾸 꺼질때 아래 코드를 기본 세팅해주시면 안꺼지고 대기합니다. 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #브라우저 꺼짐 방지 코드

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) #크롬드라이버를 최신으로 유지해줍니다.
# 그리고, 최신버전 셀레니움 문법이 바뀐거같다.

# 2. vs code에서 작업시,
# 01 - 터미널로 셀레니움 설치
pip install selenium
"""
02 - 크롬 버전과 맞는 드라이버 다운
작업 중인 py파일과 chromedriver.exe파일을 같은 폴더에 넣어주기
(에러 발생 시,
터미널을 열고 터미널 경로와 같은 위치에 드라이버를 넣어주면 됨)
"""
