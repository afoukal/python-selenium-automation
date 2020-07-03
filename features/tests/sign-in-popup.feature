# Created by Bogos at 6/28/2020
Feature: Amazon main page popup

  Scenario: Sign in pop up
    Given Open Amazon page
    Then Verify Sign in popup is present
    When Sign in popup disappears
    Then Verify Sign in popup is not clickable
