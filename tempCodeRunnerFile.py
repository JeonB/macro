
# # 아이디, 패스워드 입력
# id = driver.find_element_by_name('userId')
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