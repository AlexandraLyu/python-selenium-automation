# Created by AlexandraLyubchevska at 4/24/2024
Feature: Search and Verify Products on Target Website

  Scenario: Search for a product and verify search results
    Given Open Target main page
    When Search for laptop
    Then Verify search results are shown for laptop

  Scenario: Add product to cart and verify the cart
    Given Open Target main page
    When Search for keyboard
    And Click on Add to Cart button
    #Then Verify that Cart icon displays "1"

  Scenario: Verify the presence of product details on the search results page
    Given Open Target main page
    When Search for mouse
    Then Verify that every product has a name and an image
