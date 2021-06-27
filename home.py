import select
import time
from selenium import webdriver  #
from selenium.webdriver.chrome.options import Options
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
driver.execute_script('window.scrollBy(0,600)')
driver.find_element_by_class_name('woocommerce-LoopProduct-link').click()
driver.find_element_by_class_name('reviews_tab').click()
driver.find_element_by_class_name('star-5').click()
Review = driver.find_element_by_id('comment')
Review.send_keys('"Nice book!"')
Name = driver.find_element_by_id('author')
Name.send_keys("Pavel")
Email = driver.find_element_by_id('email')
Email.send_keys("equ@mail.com")
driver.find_element_by_id('submit').click()