Feature: Card
  As a user I want to create, display, update, and delete cards in my board

  Scenario: User can create cards
    Given the user is on a board with at least one list
    When a card is created with name 'testCard'
    Then the card is shown on the list

  Scenario: User cannot create cards without selecting a list
    Given there are no lists on the board
    When a card is created
    Then an error is shown 404

  Scenario: User cannot create cards without being authorized
    Given user does not have a token
    When the user create a card
    Then the response is 400

  Scenario: User can edit card title
    Given the user is on a board with at least one list
    When the user selects a card
    And the edits the card title to 'editTitle'
    Then the card title is updated

  Scenario: User can add a label to a card
    Given the user is on a board with at least one list
    When the user selects a card
    And the user adds a label
    Then the card is updated with the label

  Scenario: User can display a card
    Given the user is on a board with at least one list
    When the user clicks the pencil icon on the card
    And clicks 'Open card'
    Then the card is displayed

  Scenario: User can delete a card
    Given has a card in a board
    When deletes the card
    Then the card is deleted


