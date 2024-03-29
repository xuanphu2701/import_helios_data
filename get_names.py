from selenium.webdriver.common.by import By

ITEM_PER_PAGE = 20


def get_names(official_driver, page):
    res = []
    for page in range(1, page + 1):
        official_collection_url = f'https://www.nhathuochelios.com/collections/all?page={page}'
        official_driver.get(official_collection_url)

        # Find the link
        all_links = official_driver.find_elements(By.XPATH,
                                                  '//div[@class="collection-body"]//div[@class="product-title"]//a')
        all_values = [link.text for link in all_links]
        res += all_values
    return res
