# Created by aaron at 7/15/2022
Feature: Test Involving with Gettop.us Home Page
  All test involve Gettop Website Starting with Home Page

  Scenario: Verify Home Button Works Correctly
    Given Gettop Home Page
    When Mac Link is Clicked
    And Mac Page is Verify
    Then Home Button is Clicked
    And Home Page is Verified

  Scenario: Browse Our Categories Verify Functionality
    Given Gettop Home Page
    When Browse Our Categories Text is Verified
    And Verify 4 Correct Categories are Shown
    Then Click Each Category and Verify the Correct Page Opened

    Scenario: Verify the GetTop Logo takes you to home page.
      Given Gettop Home Page
      When Browse Our Categories Text is Verified
      And Mac Link is Clicked
      And Mac Page is Verify
      Then Click GetTop Logo
      And Verify Browse Our Categories Text
