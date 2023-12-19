from behave import step
from pom.results_page import ResultsPage
from utils.asserts_manager import *


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


@step("the user clicks on the first result link")
def go_to_first_result(context):
    context.results_page = ResultsPage(context.browser_interactions)
    result = context.results_page.to_first_result_page()
    assert_element_clicked(result, "First result link")