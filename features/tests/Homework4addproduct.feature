# Created by AlexandraLyubchevska at 4/12/2024
Feature: Add product to cart

Scenario: User can add a product
    Given Open Target main page
    When  Search for green tea Tazo
    Then CLick on Tazo green tea label
    Then Click on the name Tazo Green Tea Matcha Latte
    Then Click on Add to Cart button
    Then Click X button
    Then Click on the cart button
    Then Verify subtotal is $5.19



