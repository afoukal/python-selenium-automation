# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Amazon search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Dress
    Then Product results for Dress are shown
    #And First result contains skirt

  Scenario: User can select Books department
    Given Open Amazon page
    When Select stripbooks department
    And Search for Faust
    Then Books department in selected

  Scenario: User can select Baby department
    Given Open Amazon page
    When Select baby-products department
    And Search for Toys
    Then Baby department in selected