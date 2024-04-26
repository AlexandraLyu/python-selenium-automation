# Created by AlexandraLyubchevska at 4/25/2024
Feature: Add product to cart on Target website

  Scenario: User can add a Tazo Green Tea to the cart
    Given Navigate to Target main page
    When Search for Tazo green tea
    Then Click on green tea Tazo label
    Then Click on the name Tazo Green Tea
    Then Click on Add to Cart button
    Then Click X button
    Then Click on the cart button from main page
    Then Verify subtotal 5.19

    # h2.styles__StyledHeading-sc-1xmf98v-0
    # //h2[@class='']
    # //h2[contains(@class, '')]
