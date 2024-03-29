import time

from selenium.webdriver.common.by import By


def get_data(official_driver, url):
    # TODO: handle alert box
    official_driver.get(url)
    time.sleep(3)

    #Turn off the alert dialog
    try:
        official_driver.find_element(By.XPATH, '//*[@id="popup_warning"]/div/div/div/div[3]/button').click()
    except:
        pass
    name = official_driver.find_element(By.TAG_NAME, 'h1').text
    img_url = official_driver.find_element(By.XPATH, '//li[@class="thumbnail-item"]/a').get_attribute('href')
    return [name, img_url]


