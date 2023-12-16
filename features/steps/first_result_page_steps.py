from behave import step
from pom.first_result_page import FirstResultPage
from dotenv import load_dotenv
import os
from utils.asserts_manager import *


load_dotenv()


@step("the first result page is displayed")
def first_result_page_is_displayed(context):
    context.first_result_page = FirstResultPage(context.browser_interactions)
    result = context.first_result_page.is_first_result_page_visible()
    assert_page_displayed(result, "first result page")


@step("the page title contains the word 'automation'")
def title_check(context):
    context.first_result_page = FirstResultPage(context.browser_interactions)
    result = context.first_result_page.check_title()
    assert_word(result, "automation")
