import select
import time
from selenium import webdriver  #
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


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
try:
    driver.get('http://practice.automationtesting.in/')
    driver.find_element_by_id('menu-item-40').click()
    driver.execute_script("window.scrollBy(0, 300);")
    driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
    time.sleep(1)
    driver.find_element_by_class_name('amount').click()
    time.sleep(1)
    button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page-34"]/div/div[1]/div/div/div/a')))
    button.click()
    name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'billing_first_name')))
    name.send_keys('Name')
    driver.find_element_by_id('billing_last_name').send_keys('lastName')
    driver.find_element_by_id('billing_email').send_keys('equnix007@gmail.com')
    driver.find_element_by_id('billing_city').send_keys('SaintPeter')
    driver.find_element_by_id('billing_phone').send_keys('00778888999')
    driver.find_element_by_id('billing_address_1').send_keys('00778888999')
    driver.find_element_by_id('billing_state').send_keys('Ruskie')
    driver.find_element_by_id('billing_postcode').send_keys('187650')
    driver.find_element_by_id('s2id_billing_country').click()
    driver.find_element_by_id('s2id_autogen1_search').send_keys('Poland')
    time.sleep(1)
    driver.find_element_by_id('s2id_autogen1_search').send_keys(Keys.ENTER)
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)
    driver.find_element_by_id('payment_method_cheque').click()
    driver.find_element_by_id('place_order').click()
    wait = WebDriverWait(driver, 10)
    if wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), "Thank you. Your order has been received.")):
        print('WARNING COMPLETE')
    if wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-35"]/div/div[1]/table/tfoot/tr[3]/td'), "Check Payments")):
        print('COMPLETE')
finally:
    time.sleep(30)
    driver.quit()




