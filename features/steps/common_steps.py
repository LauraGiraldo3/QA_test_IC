from behave import step
from pom.home_page import HomePage
from utils.asserts_manager import *
import os
from dotenv import load_dotenv


load_dotenv()


@step("the user has accessed to Google home page")
def go_to_google(context):
    home_page = HomePage(context.browser_interactions)
    home_page.to_google(os.getenv("URL"))


@step("the user type 'test automation' into the search field")
def automation_search(context):
    context.home_page = HomePage(context.browser_interactions)
    result = context.home_page.type_search_word()
    assert_input_data(result, "Search input")


@step("the user clicks on search button")
def click_search(context):
    context.home_page = HomePage(context.browser_interactions)
    result = context.home_page.to_results_page()
    assert_element_clicked(result, "Search button")