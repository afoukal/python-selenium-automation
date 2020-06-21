# Created by Bogos at 6/21/2020
Feature: Scenarios for WholeFoods deals

  Scenario: Each product has "Regular" price field and product name
    Given Open Amazon WholeFoods Deals
    Then Each item has Regular field and Product name
