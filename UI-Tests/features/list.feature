# Created by seymafirat at 06/10/2022
Feature: Lists Creation
  As a user I want to create lists in my board

  Scenario: User can create lists
    Given user is on a board
    When user creates a list
    And user enters 'test' in the title
    Then a list is created

  Scenario: User cannot create lists without a title
    Given user is on a board
    When user creates a list
    And user leaves the title empty
    Then an error message is shown

  Scenario: User can change the list title
    Given a user is on a board with a list
    When user clicks the list title
    And enters 'changeTitle'
    Then the list name is changed to 'changeTitle'

  Scenario: User cannot change the title to empty string
    Given a user is on a board with a list
    When user clicks the list title
    And enters ''
    Then the list name is not changed

  Scenario: User can archive a list
    Given a user is on a board with a list
    When the user clicks the three dots on the list
    And the user clicks 'archive this list'
    Then the list is not displayed anymore

