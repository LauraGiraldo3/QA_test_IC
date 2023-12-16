from behave import step
from pom.results_page import ResultsPage
from dotenv import load_dotenv
import os
from utils.asserts_manager import *


load_dotenv()


@step("the user clicks on the first result link")
def go_to_first_result(context):
    context.results_page = ResultsPage(context.browser_interactions)
    result = context.results_page.to_first_result_page()
    assert_element_clicked(result, "Search button")