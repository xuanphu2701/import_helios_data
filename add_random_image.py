import random
from selenium.webdriver.common.by import By


def add_random_image(cms_driver):
    # Image name in the database has the format from 3434.jpg to 200.jpg
    img_idx = random.randint(1, 200)
    img_url = f'https://poc-helios.systems.com.vn/static/1/images/img_pool/{img_idx}.jpg'
    hidden_element = cms_driver.find_element(By.XPATH, '//input[@type="hidden"]')
    cms_driver.execute_script("arguments[0].setAttribute('value',arguments[1])", hidden_element, img_url)
