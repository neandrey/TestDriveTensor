from .pages.picture_page import ImagePage
from .pages.main_page import MainPage
import  pytest


@pytest.mark.first_picture
def test_picture_yandex(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_image_link()
    page.go_to_image_page()
    image_page = ImagePage(browser, browser.current_url)
    image_page.should_be_image_url()
    text_first_categoria = image_page.get_text_first_categoria()
    image_page.open_first_categoria()
    image_page.search_field_correct_text(text=text_first_categoria)
    image_page.should_be_first_categoria()
    image_page.open_first_image()
    image_page.click_button_next()
    image_page.click_button_prev()

