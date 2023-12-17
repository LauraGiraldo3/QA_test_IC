from utils.browser_interactions import BrowserInteractions
from pom.locators.results_page_locators import ResultsPageLocators
from pom.first_result_page import FirstResultPage


class ResultsPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def is_results_page_visible(self):
        return self.browser_interactions.element_is_visible(ResultsPageLocators.RESULTS_STATS)

    def check_results(self):
        elements_list = self.browser_interactions.get_elements(ResultsPageLocators.RESULTS)
        for element in elements_list[:3]:
            text_to_check = element.text
            if "automation" not in text_to_check.lower():
                return False
        return True

    def to_first_result_page(self):
        self.browser_interactions.click_element(ResultsPageLocators.FIRST_RESULT)
        return FirstResultPage(self.browser_interactions)



