from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def fb_page_query(query_id):
    query_id = str(query_id)

    print("Query for facebook page: https://fb.com/" + query_id)
    driver.get('https://www.like4like.org/login/')
    driver.add_cookie({'name' : 'PHPSESSID', 'value' : os.environ['SESS_ID'], 'domain' : '.like4like.org'})
    driver.get('https://www.like4like.org/login/')
    driver.get('https://www.like4like.org/user/manage-facebook.php')

    bought_credit = driver.find_element(By.ID, 'bought-credits').get_attribute('innerHTML')
    print("Current Credit:", bought_credit)

    page_specific = driver.find_element(By.XPATH, '//span[contains(text(),'+'"'+query_id+'"'+')]')
    arch_num = page_specific.find_element(By.XPATH, '../../td[2]/span').get_attribute('innerHTML')
    print("Completed Like:", arch_num)
    
    crr_status = page_specific.find_element(By.XPATH, '../../td[3]/a').get_attribute('innerHTML')
    if crr_status == "Limited":
        crr_status = "Active"
    elif crr_status == "Exhausted":
        crr_status = "Completed"
    print("Current Status:", crr_status)
    
    return [crr_status, arch_num]