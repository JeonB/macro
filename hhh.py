import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

driver_path = './chromedriver.exe'   # 본인의 chromedriver 경로를 넣어줍니다.

# 크롬 옵션을 설정해줍니다.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('window-size=1920x1080')

# 웹 드라이버에 service와 option값을 전달
s = Service(driver_path)
driver = webdriver.Chrome(service=s, options=chrome_options)

# 웹 페이지 열기
driver.get('https://www.naver.com')  # url에는 본인이 열고자하는 웹페이지 주소를 넣어주세요

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
# chrome driver의 버전 정보를 가져옵니다.

current_path = os.getcwd()
# 현재 파일의 경로를 가져옵니다.

driver_path = f'{current_path}/{chrome_ver}/chromedriver.exe'
# 현재 폴더 안에 chrome_ver(예를 들어 101.2) 폴더를 만들어 이 안에 chromedriver.exe를 다운 받도록 합니다. - 경로 지정

if not os.path.exists(driver_path):
    chromedriver_autoinstaller.install(True)
    print(f"install the chrome driver(ver: {chrome_ver})")
# 최신 버전이 아니면(해당 버전의 폴더가 없으면) 다운받습니다.