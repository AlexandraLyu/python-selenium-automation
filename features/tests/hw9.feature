# Created by AlexandraLyubchevska at 5/9/2024

  Feature: Target Sign In Page - Invalid Login Attempt

  Scenario: User attempts to sign in with incorrect email and password
    Given User opens the Target sign in page
    When User enters incorrect email and password combination
    And User clicks the login button
    Then Verify that the message "Sorry, something went wrong. Please try again." is shown
