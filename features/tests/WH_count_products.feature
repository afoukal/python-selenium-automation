# Created by Bogos at 6/14/2020
Feature: Test Scenarios for WholeFoods product count

  Scenario: Validate the quantity of the products shown on "Browse products"
    Given Open Whole Foods page
    When Click on Browse Products
    And Choose the store
    Then Number of products per page is 60
    And 4 products are shown for each category