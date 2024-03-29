import time
from selenium.webdriver.common.by import By
from add_image import add_image
from selenium.webdriver.support.ui import Select
from add_random_image import add_random_image
import random
from helper import random_select


def add_product(cms_driver, category_value, target_user_value, data):
    cms_product_url = "https://poc-helios.systems.com.vn/product/update"
    cms_driver.get(cms_product_url)
    time.sleep(1)
    # add_image(cms_driver, data[1])

    # Add random image from the prepared image pool
    add_random_image(cms_driver)

    # Add name

    # Add code
    cms_driver.find_element(By.NAME, 'code').send_keys(random.randint(1, 1000))

    cms_driver.find_element(By.NAME, 'barcode').send_keys(random.randint(1, 1000))

    manufacturer_id_select = Select(cms_driver.find_element(By.NAME, 'manufacturer_id'))
    random_select(manufacturer_id_select)

    product_type_id_select = Select(cms_driver.find_element(By.NAME, 'product_type_id'))
    random_select(product_type_id_select)

    country_id_select = Select(cms_driver.find_element(By.NAME, 'country_id'))
    random_select(country_id_select)

    cms_driver.find_element(By.NAME, 'number_register').send_keys('random number')

    cms_driver.find_element(By.NAME, 'price').clear()
    cms_driver.find_element(By.NAME, 'price').send_keys(str(random.randint(1, 500) * 1000))

    package_id_select = Select(cms_driver.find_element(By.NAME, 'package_id'))
    random_select(package_id_select)

    method_use_id_select = Select(cms_driver.find_element(By.NAME, 'method_use_id'))
    random_select(method_use_id_select)

    product_user_id_select = Select(cms_driver.find_element(By.NAME, 'product_user_id'))
    product_user_id_select.select_by_value(str(target_user_value))

    category_id_select = Select(cms_driver.find_element(By.NAME, 'category_id[]'))
    category_id_select.select_by_value(category_value)

    cms_driver.find_element(By.NAME, 'name_1').send_keys(data[0])

    cms_driver.execute_script('window.scrollBy(0, -50000)')
    time.sleep(1)

    cms_driver.find_element(By.XPATH, '//*[@id="frmUpdateProduct"]/div[1]/div/button').click()


