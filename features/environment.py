from utils.browser_interactions import BrowserInteractions
from utils.web_driver import WebDriverManager
from dotenv import load_dotenv
import os

load_dotenv()


def before_scenario(context, scenario):
    web_driver = WebDriverManager(os.getenv("CHROME_NAME")).create_driver()
    context.browser_interactions = BrowserInteractions(web_driver, 20)