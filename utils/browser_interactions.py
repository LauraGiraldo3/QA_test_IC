from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_locator(raw_locator: tuple) -> tuple:
    """Function, takes a tuple with a locator
    :param raw_locator: A tuple with a locator. First position for a string with the strategy and the second
        with the selector
    :returns: A tuple with the strategy BY object and the selector
    """
    strategy, selector = raw_locator
    strategies = {"ID": By.ID, "XPATH": By.XPATH, "CSS": By.CSS_SELECTOR}
    return strategies[strategy], selector


class BrowserInteractions:
    def __init__(self, driver: Chrome, time_out: int):
        """Constructor, takes a chrome driver instance and time out in milliseconds
        :param driver: Instance of Chrome WebDriver
        :param time_out: Number of milliseconds before time out
        """
        self._driver = driver
        self.time_out = time_out

    def open_page(self, url: str):
        """Takes a url and call method to visit the page
        :param url: String with the url to visit
        """
        self._driver.get(url)

    def click_element(self, raw_locator: tuple):
        """Click an element
        :param raw_locator: tuple with locator type and selector
        """
        element = WebDriverWait(self._driver, self.time_out).until(
            EC.element_to_be_clickable(get_locator(raw_locator))
        )
        element.click()

    def input_text(self, raw_locator: tuple, text: str) -> bool:
        """Fill an input field with a string
        :param raw_locator: Field to fill. Tuple contains two strings for the strategy and selector.
        :param text: String to put into field
        :return: True if the field was found and filled. False if field was not found.
        """
        try:
            element = WebDriverWait(self._driver, self.time_out).until(EC.visibility_of_element_located(
                get_locator(raw_locator)
            ))
        except:
            return False
        else:
            element.send_keys(text)
            return True

    def element_is_visible(self, raw_locator: tuple) -> bool:
        """Checks if an element is visible
        :param raw_locator: Tuple contains two strings for the strategy and selector for the element to check
        :returns: True if the element is visible. False if the element is not visible.
        """
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.visibility_of_element_located(get_locator(raw_locator))
            )
        except:
            return False
        else:
            return True

    def get_elements(self, raw_locator: tuple) -> list[WebElement]:
        """Gets elements by a given locator
        :param raw_locator: Tuple contains two strings for the strategy and selector for the elements
            to found
        :returns: A list with the web elements that meet the locator. A empty list if elements were not found
        """
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_all_elements_located(get_locator(raw_locator))
            )
        except:
            return []
        else:
            return self._driver.find_elements(*get_locator(raw_locator))

    def get_element(self, raw_locator: tuple) -> WebElement:
        """Gets an element given by a locator
        :param raw_locator: Tuple contains two strings for the strategy and selector for the elements
            to found
        :returns: A web element. A None value if the element was not found
        """
        try:
            WebDriverWait(self._driver, self.time_out).until(
                EC.presence_of_element_located(get_locator(raw_locator))
            )
        except:
            return None
        else:
            return self._driver.find_element(*get_locator(raw_locator))