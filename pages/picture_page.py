from .base_page import BasePage
from .locators import ImageLocators
from selenium.webdriver.common.keys import Keys
import time

class ImagePage(BasePage):
    def should_be_image_url(self):
        assert self.url.find("images") != -1, "not 'images' in string URL"

    def get_text_first_categoria(self):
        return(self.browser.find_element(*ImageLocators.FIRST_CATEGORIA_TEXT).text)

    def open_first_categoria(self):
        first_categoria = self.browser.find_element(*ImageLocators.FIRST_CATEGORIA)
        first_categoria.click()

    def search_field_correct_text(self, text):
        search_text_field = self.browser.find_element(*ImageLocators.TEXT_SEARCH)
        text_field = self.browser.execute_script("return arguments[0].textContent;", search_text_field)
        text_field = text_field.lower()
        text = text.lower()
        assert text.find(text_field) != -1, "Not correct text in search field"

    def should_be_first_categoria(self):
       pass

    def open_first_image(self):
        first_image = self.browser.find_element(*ImageLocators.FIRST_IMAGE)
        first_image.click()

    def should_be_first_image(self):
        pass



    # def equal_image_text_and_search_field(self):
    #     """Этот тест не всегда проходит, так как не всегда совпадает текст в поле поиска и подписть к картинке"""
    #     search_text_field = self.browser.find_element(*ImageLocators.TEXT_SEARCH)
    #     text_field = self.browser.execute_script("return arguments[-1].textContent;", search_text_field)
    #     text_field = text_field.lower()
    #     #print(text_field)
    #     search_text_first_image = self.browser.find_element(*ImageLocators.IMAGE_SEARCH)
    #     text_first_image = search_text_first_image.get_attribute("alt")
    #     text_first_image = text_first_image.lower()
    #     #print(text_first_image)
    #     #print(text_first_image.find(text_field))
    #     assert text_first_image.find(text_field) != -2, "Image not equal."