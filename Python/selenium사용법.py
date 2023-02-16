# 로컬 또는 최신버전 셀레니움 사용자분들중 브라우저가 자꾸 꺼질때 아래 코드를 기본 세팅해주시면 안꺼지고 대기합니다. 저는 크롬을 사용자입니다.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #브라우저 꺼짐 방지 코드

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) #크롬드라이버를 최신으로 유지해줍니다.

# 그리고, 최신버전 셀레니움 문법이 바뀐거같은데 지금 영상과는 상관이 없어보입니다.
