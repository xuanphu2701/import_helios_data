from selenium.webdriver.common.by import By
from extract_capcha import extract_capcha


cms_url = "https://poc-helios.systems.com.vn"


def login_helios(cms_driver, username, password):
    cms_driver.save_screenshot('img/screenshot.png')

    # Login
    cms_driver.find_element(By.NAME, 'username').send_keys(username)
    cms_driver.find_element(By.NAME, 'password').send_keys(password)

    capcha = extract_capcha('img/screenshot.png')
    cms_driver.find_element(By.NAME, 'captcha').send_keys(capcha)

    if cms_driver.current_url == cms_url:
        cms_driver.find_element(By.LINK_TEXT, 'Đăng nhập').click()

    if cms_driver.current_url == cms_url:
        cms_driver.quit()