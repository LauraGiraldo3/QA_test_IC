from behave import step
from pom.home_page import HomePage
from utils.asserts_manager import *


@step("the Google home page is displayed")
def home_page_is_displayed(context):
    context.home_page = HomePage(context.browser_interactions)
    result = context.home_page.is_home_visible()
    assert_page_displayed(result, "home")






