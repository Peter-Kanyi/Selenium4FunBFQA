from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Add_to_Cart(web_url,item_name):
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(web_url)
        time.sleep(5)

        # searching for the product to add to the cart
        search_bar = driver.find_element("name", "search")
        search_bar.send_keys(item_name)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)

        # click and add the fond item to cart
        # item_link = driver.find.element (By.PARTIAL_LINK_TEXT, Banana Cat Toy)
        # item_link.click()

        add_to_cart_button = driver.find_element(By.ID, "button_cart")
        add_to_cart_button.click()

        wait = WebDriverWait(driver, 10)
        success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success-message")))
        print("Item added to cart successfully:", success_message.text)

    finally:
        driver.quit()

# initialize
web_url = "http://opencart.qatestlab.net/"
item_name = "Banana Cat Toy"

# call the function
Add_to_Cart(web_url,item_name)