def assert_page_displayed(result: bool, page: str):
    assert result, f"{page} is not displayed"


def assert_input_data(result: bool, field_name: str):
    assert result, f"{field_name} was not filled"


def assert_element_clicked(result: bool, element: str):
    assert result, f"{element} was not found"


def assert_word(result: bool, word: str):
    assert result, f"'{word}' word is not in the results"
