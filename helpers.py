import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import time, random
import logging

logging.basicConfig(level=logging.INFO)



class Helper:

    ##======================== FUNCTION FOR CREATING A WEBSITE ==================

    def open_browser(self):
        options = uc.ChromeOptions()
        options.binary_location = r"C:\chrome-win64\chrome.exe"              #insert location of chrome tester
        #options.add_argument(r"--user-data-dir=C:\maxxy_scraper11")
        options.add_argument("--start-maximized")

        atmp = 1
        atmps = 5
        while atmp <= atmps:
            try:
                driver = uc.Chrome(options=options, version_main=150)
                wait = WebDriverWait(driver, 40)
                logging.info("Browser is OPENED")
                break
            except Exception as e:
                logging.info(f"Browser opening exception == {e}")
                if atmp == atmps:
                    logging.info("Retrying not helping, let's wait for 2 mins ...")
                    time.sleep(120)
                    atmp = 1
                else:
                    logging.info("Retrying in 20 secs ...")
                    atmp += 1
                    time.sleep(20)
                    print("starting ...")
        return driver, wait

    
    ##================= FUNCTION FOR LOADING SITE =====================

    def load_site(self, driver, url):
        atmp = 1
        atmps = 5
        while atmp <= atmps:
            try:
                driver.get(url)
                logging.info("driver.get success")
                break
            except WebDriverException:
                logging.info("Driver.get excetion")
                if atmp == atmps:
                    logging.info("Retrying not working, let's wait for 2 min ...")
                    time.sleep(120)
                    atmp = 1
                else:
                    logging.info("Retrying in 20 secs ...")
                    time.sleep(20)
                    atmp += 1
                    print("load start")

        return driver