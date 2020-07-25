# Created by Bogos at 7/19/2020
Feature: Test for products

  Scenario: Size tooltips is shown upon hovering over Add to cart button
    Given Open Amazon B074TBCSC8 product page
    When Hover over Add to Cart button
    Then Verify size selection tooltip is shown


  Scenario: New arrivals deals are displayed
    Given Open Amazon B074TBCSC8 product page
    When Hover over New Arrivals
    Then New Arrivals option list is displayed