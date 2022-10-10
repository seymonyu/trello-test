# Created by seymafirat at 06/10/2022
@api
Feature: Lists Creation
  As a user I want to create lists in my board

  Background: User has a token for authorization
    Given I am an authorized user

  @api
  Scenario: User can create lists
    Given there is a board
    When user creates a list
    Then a list is created


  Scenario: User can display a list
    Given the api endpoint is set
    When the request HEADER is set\
    And GET HTTP request is sent
    Then the response <statusCode> is 200


  Scenario: User cannot create lists without a title
    Given user is on a board
    When user creates a list
    And user leaves the title empty
    Then the list is not created
  @api
  Scenario: User can change the list title
    Given a user is on a board with a list
    When user clicks the list title
    And enters 'changeTitle'
    Then the list name is changed to 'changeTitle'
  @api
  Scenario: User can archive a list
    Given a user is on a board with a list
    When the user clicks the three dots on the list
    And the user clicks 'archive this list'
    Then the list is not displayed anymore

