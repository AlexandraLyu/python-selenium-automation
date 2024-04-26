# Created by AlexandraLyubchevska at 4/25/2024

Feature: Verify Sign In Functionality on Target Website

Scenario: Verify user can access Sign In from the right side navigation
    Given the user is on the Target home page
    When the user clicks on Sign In from the top navigation
    Then the user clicks on Sign In from the right side navigation
    Then the Sign In form should be opened
