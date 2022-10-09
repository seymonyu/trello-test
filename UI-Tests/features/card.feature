Feature: Card
  As a user I want to create, display, update, and delete cards in my board

  Scenario: User can create cards
    Given the user is on a board with at least one list
    When the user clicks 'Add card'
    And the user enters 'myCard'
    Then the card is created

  Scenario: User can edit card title
    Given the user is on a board with at least one list
    When the user selects a card
    And the edits the card title to 'editCard'
    Then the card title is updated

  Scenario: User can add a label to a card
    Given the user is on a board with at least one list
    When the user selects a card
    And the user clicks the 'Labels'
    And the user selects the first label
    Then the card is updated with the label

  Scenario: User can display a card
    Given the user is on a board with at least one list
    When the user clicks the pencil icon on the card
    And clicks 'Open card'
    Then the card is displayed

Scenario: User can archive a card
    Given the user is on a board with at least one list
    When the user clicks the pencil icon on the card
    And clicks 'Archive'
    Then the card is archived

  Scenario: User can delete a card
    Given user is opened a card
    When the user clicks 'Archive card' button
    And the user clicked 'Delete' button
    Then the card is deleted

