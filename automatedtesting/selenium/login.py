# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging

# Start the browser and login with standard_user
def login (user, password):
    logging.basicConfig(filename='selenium.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
     
    logging.info('Starting the browser...')
    #print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    chromedriver = "/usr/lib/chromium-browser/chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    logging.info('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element("id",'user-name').send_keys(user)
    driver.find_element("id",'password').send_keys(password)
    driver.find_element("id",'login-button').click()
    logging.info('Login successfully')

    logging.info('Choose all items')
    items = driver.find_elements("class name",'inventory_item')
    for item in items:
        name = item.find_element("class name",'inventory_item_name')
        logging.info('Add ' + name.text + ' to cart')
        item.find_element("class name",'btn_inventory').click()
    
    logging.info('Go to cart')
    driver.find_element("class name",'shopping_cart_link').click()
    removes = driver.find_elements("class name", "cart_item")
    for remove in removes:
        name = remove.find_element("class name",'inventory_item_name')
        logging.info('Remove ' + name.text + ' from cart')
        remove.find_element("class name",'cart_button').click()

    logging.info('Done')

login('standard_user', 'secret_sauce')

