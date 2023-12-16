from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


class WebDriverManager:
    def __init__(self, driver_name: str):
        self.driver_name = driver_name

    def create_driver(self) -> Chrome:
        if self.driver_name == "Chrome headless":
            options = ChromeOptions()
            options.add_argument("--headless=new")
            driver = Chrome(options=options)
            return driver

        elif self.driver_name == "Chrome":
            return Chrome()