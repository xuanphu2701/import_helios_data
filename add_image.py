from selenium.webdriver.common.by import By


def add_image(cms_driver, img_url):
    hidden_element = cms_driver.find_element(By.XPATH, '//input[@type="hidden"]')
    cms_driver.execute_script("arguments[0].setAttribute('value',arguments[1])", hidden_element, img_url)
