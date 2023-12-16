import os
from utils.browser_interactions import BrowserInteractions
from pom.locators.home_page_locators import HomeLocators
from pom.results_page import ResultsPage


class HomePage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def to_google(self, url: str):
        self.browser_interactions.open_page(url)

    def is_home_visible(self):
        return self.browser_interactions.element_is_visible(HomeLocators.SEARCH_FORM)

    def type_search_word(self):
        return self.browser_interactions.input_text(HomeLocators.INPUT_FIELD, os.getenv("WORD_TO_SEARCH"))

    def to_results_page(self):
        self.browser_interactions.click_element(HomeLocators.SEARCH_BUTTON)
        return ResultsPage(self.browser_interactions)
