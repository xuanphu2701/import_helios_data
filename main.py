import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import math
from loginHelios import login_helios
from get_category_list import get_category_list
from add_product import add_product
from get_data import get_data
from get_names import get_names
from get_urls import get_urls

USERNAME = 'shop_admin'
PASSWORD = 'Adminadmin@789'
CHROME_DRIVER_PATH = "D:/Tools/chromedriver-win64/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=900x1080")

chrome_service = Service(executable_path=CHROME_DRIVER_PATH)
cms_driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
official_driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

startSetUp = time.time()

cms_url = "https://poc-helios.systems.com.vn"
cms_driver.get(cms_url)
time.sleep(2)
login_helios(cms_driver, USERNAME, PASSWORD)

category_value_list = get_category_list(cms_driver)

# page equal to the number of category multiply number of user kind (ex: Người lớn)
# and divided by the number of item in each page
page = math.ceil(len(category_value_list)*3/20)
# urls = get_urls(official_driver, page)
names = get_names(official_driver, page)
# Shuffle the names to reduce repeated item
random.shuffle(names)

endSetup = time.time()
print('Login successfully')
print(f'The setup time is {endSetup - startSetUp}')
startAdd = time.time()

idx = 0
for category in category_value_list:
    for target_user_value in range(1, 4):
        # data = get_data(official_driver, urls[url_idx])
        add_product(cms_driver, category, target_user_value, [names[idx], None])
        idx +=1
        print(f'Finish add item {idx}: target_user {target_user_value} and category {category}')


endAdd = time.time()
print(f'Finish importing data, the import time is {endAdd - startAdd}')

cms_driver.quit()
official_driver.quit()