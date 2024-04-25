#Created by AlexandraLyubchevska at 4/11/2024
Feature: Empty Cart Message Verification

Scenario: Verify "Your cart is empty" message is shown
Given I am on the target.com website
When I click on the Cart icon
Then I should see the message "Your cart is empty"