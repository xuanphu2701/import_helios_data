from selenium.webdriver.common.by import By


def get_category_list(cms_driver):
    """
    Extract category list (value)
    :param cms_driver:
    :return: category value list
    """
    cms_driver.get('https://poc-helios.systems.com.vn/product/update')
    category_elements = cms_driver.find_elements(By.XPATH, "//select[@name='category_id[]']/option")
    category_list = [el.get_attribute('value') for el in category_elements]
    return category_list
