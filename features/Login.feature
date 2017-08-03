Feature: Login as Admin
  @debug
  Scenario: Login as correct Admin
    Given I have language set as English
    When I type correct "user"
    And I type correct "password"
    And I click on login
    Then I can see my "role"

  Scenario: Go to Administration Page
    Given I am on homepage
    When I click on Admin Tab
    Then I can see Admin Overview

  Scenario: User able to scroll left hand menu if results less than the height of menu
    Given I am on admin tab
    When I search for Invalid User
    Then I should be able to scroll and see Hardware

  @retest
  Scenario: User is able to revert suspension
    Given I am on Admin Tab
    When I search for a user by username and click on it
    And I suspend the user
    And I unsuspend the user
    Then I can see user active

  @debug
  Scenario: User is able to see Active Emergency Latest First
    Given I am on active Emergency Center
    Then I am able to see latest emergency first

