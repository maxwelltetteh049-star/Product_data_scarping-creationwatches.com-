from helpers import Helper
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import mysql.connector
import logging
import time, random
import re
import csv

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

#---------------object for calling the functions in the helper.py -------------
helper = Helper()

#----------- container for storing scraped links -----------
links = []

# Element extraction code.

def safe_find(driver, xpath):
    try:
        return driver.find_element(By.XPATH,xpath).text
    except:
        return None
    
##======  connecting mysql database to python =============
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "passworDmax15$",
    database = "webscraping_db"
)
cursor = conn.cursor()
cursor.execute("ALTER TABLE watches ADD UNIQUE(detail_link)")




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

##=================== LOOPING THROUGH THE LISTING PRODUCTS AND EXTRACTING THEIR DETAIL PAGE LINK =============
for index in range(len(products)):
    try:
        product = products[index]
    except IndexError:
        logging.info("Index out of range breakinng loop")
        break

    try:
        d_link = product.find_element(By.XPATH,".//a[@class='imgBox']").get_attribute("href")
    except:
        d_link = None
    
    print(d_link)
    if d_link is not None:
        links.append(d_link)

##===================== LOOPING THROUGH THE DETAIL LINKS STORED AND VISITING EACH OF THEM =============
for index in range(len(links)):
    try:
        detail_link = links[index]
    except IndexError:
        logging.info("Index out of range, breaking loop")

    driver = helper.load_site(driver, detail_link)

    title = safe_find(driver, "//div[contains(@class,'ProductDetails')]//h1")
    marked_price = safe_find(driver, "//div[contains(@class,'ProductDetails')]//del")
    ##---for model section
    model1 = safe_find(driver, "//div[contains(@class,'ProductDetails')]//span[contains(text(),'Model')]/parent::div")
    try:
        match = re.search(r"Model:\s*([a-zA-Z0-9\-]+)", model1)
        
        model = match.group(1)
    except:
        model = model1

    try:
        spec_btn = driver.find_element(By.XPATH,"//button[contains(text(),'Specifications')]")
    except:
        logging.debug("spec not found")
        input("stark ?")

    driver.execute_script("arguments[0].scrollIntoView({block:'centre'});", spec_btn)
    driver.execute_script("arguments[0].click()", spec_btn)

    movement = safe_find(driver, "//span[text()='Movement']/following-sibling::span")
    resistance = safe_find(driver, "//span[text()='Water Resistance']/following-sibling::span")

    #info = f'''
#title = {title}
#m_price = {marked_price}
#model = {model}
#movement = {movement}
#resistance = {resistance}
#link = {detail_link}
#'''
    #print(info)

    infoo = (title, marked_price, model, movement, resistance, detail_link)
    query = '''
INSERT IGNORE INTO watches(title, marked_price, model_no, movement, resistance, detail_link)
VALUES(%s, %s, %s, %s, %s, %s)
'''
    cursor.execute(query, infoo)
    conn.commit()
    print(f"Extracted and stored data for product {index+1}")
    

#loadING stored data back to python
query1 = "SELECT * FROM watches"
cursor.execute(query1)
data = cursor.fetchall()

# saving scraped data into csv file
filename = "products.csv"
with open(filename, "w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Marked Price", "Model_no", "Movement", "Resistance", "Detail Link"])
    writer.writerows(data)

logging.info("SCRAPINGG IS A SUCCESS")


