Feature: Card
  As a user I want to create, display, update, and delete cards in my board

  Scenario: User can create cards
    Given the user is on a board with at least one list
    When a card is created
    Then the card is shown on the list

  Scenario: User cannot create cards without selecting a list
    Given there are no lists on the board
    When a card is created
    Then an error is shown

  Scenario: User cannot create cards without logging in
    Given the trello website is opened
    When the user is not logged in
    Then the user cannot create a card

  Scenario: User can edit card title
    Given the user is on a board with at least one list
    When the user selects a card
    And the edits the card title to 'test edit'
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

  Scenario: User can archive a card
    Given the user is on a board with at least one list
    When the user clicks the pencil icon on the card
    And clicks 'Archive'
    Then the card is archived