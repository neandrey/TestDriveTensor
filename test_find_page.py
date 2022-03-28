from .pages.main_page import MainPage
import pytest

SEARCH_TEXT = "Тензор"

@pytest.mark.need_review
def test_guest_can_find_five_link_tensor(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_find_field()
    page.enter_data_in_search_field(name=SEARCH_TEXT)
    page.should_be_table_prompt()
    page.click_enter_in_search_field()
    page.tensor_ru_in_first_five_link()




