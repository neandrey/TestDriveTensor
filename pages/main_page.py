from .base_page import BasePage
from .locators import MainLocators
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):
    def enter_data_in_search_field(self, name):
        find_field = self.browser.find_element(*MainLocators.SEARCH_FIELD)
        find_field.send_keys(name)


    def should_be_find_field(self):
        assert self.is_element_present(*MainLocators.SEARCH_FIELD), "Find field not presented"


    def should_be_table_prompt(self):
        assert self.is_element_present(*MainLocators.PROMPT_TABLE), "Table prompt not presented"


    def click_enter_in_search_field(self):
        find_field = self.browser.find_element(*MainLocators.SEARCH_FIELD)
        find_field.send_keys(Keys.ENTER)


    def tensor_ru_in_first_five_link(self):
        elements = self.browser.find_elements(*MainLocators.TENSOR_LINK)
        for i in range(5):
            str_href = elements[i].get_attribute("href")
            assert str_href.find("tensor.ru") != -1, f"Number element {i+1} " \
                                                     f"This href={str_href} not reference tensor.ru"


    def should_be_image_link(self):
        assert self.is_element_present(*MainLocators.IMAGE_LINK), "Find picture link not presented"


    def go_to_image_page(self):
        picture_link = self.browser.find_element(*MainLocators.IMAGE_LINK)
        picture_link.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
