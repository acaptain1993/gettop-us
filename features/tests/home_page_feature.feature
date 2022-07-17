# Created by aaron at 7/17/2022
Feature: Test Involving with Gettop.us Home Page
  # Enter feature description here

  Scenario: Verify Home Button Works Correctly
    Given Gettop Home Page
    When Mac Link is Clicked
    And Mac Page is Verify
    Then Home Button is Clicked
    And Home Page is Verified