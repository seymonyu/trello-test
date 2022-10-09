Feature: Board
  As a user I want to create, display, update, and delete boards on Trello

  Scenario: User can create boards
    Given the user is on logged in on trello website
    When the user clicks on 'Create'
    And the user clicks on 'Create a board'
    And the user enters the title 'testBoard'
    Then a board is created


  Scenario: User cannot create boards without logging in
    Given the user is on trello website
    When the user is not logged in
    Then the Create board button is not available


 Scenario: User can display a board
    Given the user is on logged in on trello website
    When the user clicks on 'testBoard'
    Then the board with title 'testBoard' is displayed


  Scenario: User can change the board name
    Given the user is on logged in on trello website
    And the user is on board "testBoard"
    When the user clicks the board title
    And the user enters "updatedTitle"
    Then the board title is updated to 'updateTitle'

  Scenario: User can close a board
    Given the user is on logged in on trello website
    And the user is on board "updatedTitle"
    When the user clicks the three dots on the right of the screen
    And the user clicks more
    And the user clicks close board
    Then the board is closed

  Scenario: User can delete a board
    Given the user just closed a board
    When the user clicks 'Permanently delete board'
    And the user clicks 'Delete' on the popup
    Then the board is deleted
    And the user is taken to the main screen