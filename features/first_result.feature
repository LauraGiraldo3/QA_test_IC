Feature: Go to first result of Google search
  As a user
  I want to make a Google search
  In order to open the first result

  Background: Make a Google search
    Given the user has accessed to Google home page
    And the user type 'test automation' into the search field
    And the user clicks on search button

  @first_result
  Scenario: Go to first result page
    When the user clicks on the first result link
    Then the first result page is displayed
    And the page title contains the word 'automation'