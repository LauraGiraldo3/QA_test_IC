import os
from utils.browser_interactions import BrowserInteractions
from pom.locators.first_result_page_locators import FirstResultPageLocators


class FirstResultPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def is_first_result_page_visible(self):
        return self.browser_interactions.element_is_visible(FirstResultPageLocators.TITLE)

    def check_title(self):
        title = self.browser_interactions.get_element(FirstResultPageLocators.TITLE)
        text_to_check = title.text
        if "automation" in text_to_check.lower():
            return True
        else:
            return False