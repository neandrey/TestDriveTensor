from selenium.webdriver.common.by import By

class MainLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    PROMPT_TABLE = (By.CSS_SELECTOR, ".mini-suggest__overlay_visible")
    IMAGE_LINK = (By.XPATH, "//a[contains(@data-id, 'images')]")
    TENSOR_LINK = (By.XPATH, "//div[contains(@class, 'composite bno')]//a[contains(@target, '_blank')]")

class ImageLocators():
    FIRST_CATEGORIA = (By.XPATH, "//div[contains(@class, 'Item_pos_0')]")
    FIRST_CATEGORIA_TEXT = (By.XPATH, "//div[contains(@class, 'PopularRequestList-SearchText')]")
    TEXT_SEARCH = (By.XPATH, "//li[contains(@class, 'mini-suggest')]//b")
    FIRST_IMAGE = (By.XPATH, "//div[contains(@class, 'item__preview')]//a[contains(@class, 'item__link')]")


