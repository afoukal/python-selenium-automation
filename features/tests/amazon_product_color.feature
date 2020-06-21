# Created by Bogos at 6/21/2020
Feature: Scenarios for Amazon products

  Scenario: Product has all color options
    Given Open Amazon B07BJKRR25 product page
    Then All expected color options are present
