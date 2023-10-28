from selenium import webdriver
# from selenium.webdriver.common import By
import time
from selenium.webdriver.common.keys import Keys

def search_an_item(search_term, site_url, screenshot):
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(site_url)
        time.sleep(5)                   # Allow user time to see the site
        search_bar = driver.find_element("name","search")
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.save_screenshot(screenshot_name) # save the results
    finally:
        driver.quit()

# initialize
search_term = "Banana Cat Toy"
screenshot_name = "results/search_results.png"
site_url = "http://opencart.qatestlab.net/"

# let's call the function
search_an_item(search_term, site_url,screenshot_name)


