# Created by Bogos at 5/31/2020
Feature: Test Scenarios for Amazon Orders sign in functionality


  Scenario: User redirected to Sign in page, after clicking on Orders
    Given Open Amazon page
    When When click on orders
    Then Sign-In logo is displayed
    And Page title is correct