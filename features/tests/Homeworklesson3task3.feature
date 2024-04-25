#Created by AlexandraLyubchevska at 4/11/2024
Feature: Sign In to Target.com

    Scenario: Navigate to Sign In form from the homepage
    Given I am on the website
    When I click on the Sign In button
    And I click on the Sign In link from the right side navigation menu
    Then I should see the Sign In form opened