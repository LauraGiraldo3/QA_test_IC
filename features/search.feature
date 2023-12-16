Feature: Google search
  As a user
  I want to go to Google home page
  In order to make a search

  Background: Go to Google home page
    Given the user has accessed to Google home page
    Given the Google home page is displayed

  @google_search
  Scenario: Make a Google search
    When the user type 'test automation' into the search field
    And the user clicks on search button
    Then the search results page is displayed
    And the first 3 results contain the word 'automation'


