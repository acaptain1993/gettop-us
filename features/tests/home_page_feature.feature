# Created by aaron at 7/15/2022
Feature: Test Involving with Gettop.us Home Page
  All test involve Gettop Website Starting with Home Page

  Scenario: Verify Home Button Works Correctly
    Given Gettop Home Page
    When Mac Link is Clicked
    And Mac Page is Verify
    Then Home Button is Clicked
    And Home Page is Verified