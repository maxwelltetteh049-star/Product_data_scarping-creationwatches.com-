from helpers import Helper
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time, random

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

#---------------object for calling the functions in the helper.py -------------
helper = Helper()




driver, wait = helper.open_browser()
driver = helper.load_site(driver, "https://www.creationwatches.com/products/bestseller-watches")

# you can navigate the site to categories here _________

try:
    products = wait.until(
        EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'productBox')]"))
    )
except:
    logging.info("Container not found !!")
    input("stark")

#scrolling
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(1,3))

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

products = driver.find_elements(By.XPATH,"//div[contains(@class,'productBox')]")

time.sleep(3333)

