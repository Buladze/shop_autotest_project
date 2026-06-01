from .base_page import BasePage
from .data import MainPageData

class MainPage(BasePage): 
    def should_be_main_page(self):
        self.verify_url(MainPageData.URL_PAGE)
        