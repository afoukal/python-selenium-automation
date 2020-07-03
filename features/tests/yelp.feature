# Created by Bogos at 6/28/2020
Feature: Window handing

  Scenario: Company site is open in the new page
    Given Open Yelp web page
    When Click on restaurant web page
    And Verify the new window was opened
    Then Close new window and return to Yelp