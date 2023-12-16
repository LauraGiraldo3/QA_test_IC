from behave import step
from pom.home_page import HomePage
from pom.results_page import ResultsPage
from dotenv import load_dotenv
import os
from utils.asserts_manager import *


load_dotenv()


@step("the user has accessed to Google home page")
def go_to_google(context):
    home_page = HomePage(context.browser_interactions)
    home_page.to_google(os.getenv("URL"))


@step("the Google home page is displayed")
def home_page_is_displayed(context):
    context.home_page = HomePage(context.browser_interactions)
    result = context.home_page.is_home_visible()
    assert_page_displayed(result, "home")


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


@step("the search results page is displayed")
def results_page_is_visible(context):
    context.results_page = ResultsPage(context.browser_interactions)
    result = context.results_page.is_results_page_visible()
    assert_page_displayed(result, "results page")


@step("the first 3 results contain the word 'automation'")
def results_check(context):
    context.results_page = ResultsPage(context.browser_interactions)
    result = context.results_page.check_results()
    assert_word(result, "automation")