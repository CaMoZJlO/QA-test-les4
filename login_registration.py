import select
import time
from selenium import webdriver  #
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



path_to_extension = r'C:\Users\equni\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.34.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(10)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.implicitly_wait(5)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.close()
job = driver.window_handles[0]
driver.switch_to.window(job)
driver.get('http://practice.automationtesting.in/')
driver.find_element_by_id('menu-item-50').click()
driver.find_element_by_id('reg_email').click()
email = driver.find_element_by_id('reg_email')
email.send_keys('equnix007@gmail.com')
search_form = driver.find_element_by_id('reg_password')
search_form.send_keys('equnixQA007')
search_form.click()
search_form.send_keys(Keys.SHIFT)
driver.implicitly_wait(10)
driver.find_element_by_id('body').click()
driver.find_element_by_class_name('register').click()
driver.implicitly_wait(10)
driver.execute_script( "window.open();" )
logins = driver.window_handles[0]
driver.switch_to.window(logins)
driver.close()
logines = driver.window_handles[0]
driver.switch_to.window(logines)
driver.get('http://practice.automationtesting.in/')
driver.find_element_by_id('menu-item-50').click()
email = driver.find_element_by_id('username')
email.send_keys('equnix007@gmail.com')
search_form = driver.find_element_by_id('password')
search_form.send_keys('equnixQA007')
driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
if WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,'Sign out'))):
    print('Элемент есть')