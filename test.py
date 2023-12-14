import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import pyperclip
import pyautogui
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('window-size=1920x1080')

# chrome driver의 버전 정보를 가져옵니다.
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
current_path = os.getcwd()
driver_path = f'{current_path}/{chrome_ver}/chromedriver.exe'

# 웹 드라이버에 service와 option값을 전달
s = Service(driver_path)
driver = webdriver.Chrome(service=s, options=chrome_options)

if not os.path.exists(driver_path):
    chromedriver_autoinstaller.install(True)
    print(f"install the chrome driver(ver: {chrome_ver})")
# 셀레니움 열기
driver.get('https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login')
# 아이디, 패스워드 입력
driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='loginAllWrap']/div[2]/iframe"))
id = driver.find_element(By.ID,'userId')
id.click()
pyperclip.copy("test")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
# id.send_keys('your_id')
# password = driver.find_element_by_name('userPwd')
# password.send_keys('your_password')

# # 로그인 버튼 클릭
# login_button = driver.find_element_by_css_selector('#logstatus > a.login > img')
# login_button.click()
# driver.implicitly_wait(5)

# # 티켓 예약 사이트로 이동
# driver.get('https://tickets.interpark.com/goods/23004629')

# # 날짜 선택
# date_button = driver.find_element_by_xpath("//button[@data-value='2023-04-01']")
# date_button.click()
# driver.implicitly_wait(5)

# # 회차 선택
# time_selector = driver.find_element_by_css_selector('li.time:nth-child(2) > a:nth-child(1) > img:nth-child(1)')
# time_selector.click()
# driver.implicitly_wait(5)

# # 예매하기 버튼 클릭
# book_button = driver.find_element_by_css_selector('#SmallNextBtn')
# book_button.click()
# driver.implicitly_wait(5)

# # 좌석 선택
# seat_button = driver.find_element_by_css_selector('#ifrmSeat > div.seatL > ul > li:nth-child(2) > div > a')
# seat_button.click()
# driver.implicitly_wait(5)

# # 좌석 선택 완료 버튼 클릭
# seat_select_button = driver.find_element_by_css_selector('#ifrmSeatDetail > div.wrap_bk_btn > a')
# seat_select_button.click()
# driver.implicitly_wait(5)

# # 매수 선택
# ticket_num_selector = Select(driver.find_element_by_css_selector('#CountSelect'))
# ticket_num_selector.select_by_visible_text('1')
# driver.implicitly_wait(5)

# # 다음단계 버튼 클릭
# next_button1 = driver.find_element_by_css_selector('#LargeNextBtn')
# next_button1.click()
# driver.implicitly_wait(5)

# # 생년월일 입력
# birth_year = driver.find_element_by_css_selector('#YY')
# birth_year.send_keys('1994')
# birth_month = driver.find_element_by_css_selector('#MM')
# birth_month.send_keys('08')
# birth_day = driver.find_element_by_css_selector('#DD')
# birth_day.send_keys('10')
# driver.implicitly_wait(5)

# # 다음단계 버튼 클릭
# next_button2 = driver.find_element_by_css_selector('#LargeNextBtn')
# next_button2.click()
# driver.implicitly_wait(5)

# # 무통장입금 선택
# payment_option_button = driver.find_element_by_css_selector('#PayMethodList > li:nth-child(2) > label')
# payment_option_button.click()
# driver.implicitly_wait(5)

# # 입금 은행 선택
# bank_selector = Select(driver.find_element_by_css_selector('#BankCode'))
# bank_selector.select_by_visible_text('은행이름')
# driver.implicitly_wait(5)

# # 다음단계 버튼 클릭
# next_button3 = driver.find_element_by_css_selector('#LargeNextBtn')
# next_button.click()
# driver.implicitly_wait(5)

# # 체크 버튼 클릭
# check_button = driver.find_element_by_css_selector('#Agree')
# check_button.click()
# driver.implicitly_wait(5)

# # 결제하기 버튼 클릭
# pay_button = driver.find_element_by_css_selector('#LargeNextBtn')
# pay_button.click()