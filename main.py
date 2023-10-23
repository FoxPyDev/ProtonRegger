import time
from Generator import generate_password, generate_abstract_username
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://account.proton.me/ru/mail/signup?plan=free&billing=12&minimumCycle=12&currency=EUR&ref=prctbl')
time.sleep(10)
generated_username = generate_abstract_username(12)
generated_password = generate_password(10)

frame = browser.find_element(By.CLASS_NAME, 'challenge-width-increase.h-custom')

browser.switch_to.frame(frame)
time.sleep(3)
username_input = browser.find_element(By.CSS_SELECTOR, '#email')
time.sleep(3)
username_input.send_keys(generated_username)
time.sleep(3)
browser.switch_to.default_content()
time.sleep(3)
password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
repeat_password_input = browser.find_element(By.XPATH, '//*[@id="repeat-password"]')
create_account_button = browser.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/form/button')
time.sleep(2)
password_input.click()
time.sleep(2)
password_input.send_keys(generated_password)
time.sleep(5)
repeat_password_input.click()
time.sleep(2)
repeat_password_input.send_keys(generated_password)
time.sleep(5)
create_account_button.click()
time.sleep(60)
