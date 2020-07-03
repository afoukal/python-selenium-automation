# Created by Bogos at 6/28/2020
Feature: Amazon today's deals

  Scenario: User can open and close Today's deals under $25
    Given Open Amazon page
    When Store original windows
    And Click to open Today's Deals in new tab
    And Switch to the newly opened window
    And Choose Under 25
    Then Verify that deals under 25 are shown
    When User put any product into a cart
    And Close new window and can switch back to original
    And Refresh the page
    Then Cart has 1 item
