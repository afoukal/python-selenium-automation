# Created by Bogos at 6/14/2020
Feature: Validate Best Sellers Header

  Scenario: Validate the quantity of the links in the header
      Given Open Amazon Best Sellers page
      Then Check that 5 links are present


  Scenario: Validate that each link in the header, navigate to correct page
      Given Open Amazon Best Sellers page
      Then Click on each link and validate the header