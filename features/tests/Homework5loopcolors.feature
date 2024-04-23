# Created by AlexandraLyubchevska at 4/23/2024
Feature: Verify color selection on product page
  This feature describes the validation of color selection for a bath towel set on the Target website.

  Scenario: Verify color selection for bath towel set
    Given I navigate to "https://www.target.com/p/quick-dry-ribbed-bath-towel-set-threshold/-/A-81917187?preselect=81781514#lnk=sametab"
    When Loop through colors and verify selection
    Then Verify when clicking on the color selection the correct color image is displayed
