Feature: Login
  As a user
  I want to log in to Trello

  Scenario: User can login the trello
    Given A user is on the trello website
    When the user clicks Log in
    And the user enters a valid email <email> and password <password>
    And the user clicks Log in
    Then the should be successfully logged into the site

  Scenario: User cannot login the trello with wrong password
    Given A user is on the trello website
    When the user clicks Log in
    And the user enters a valid email <email> and the wrong password <password>
    And the user clicks Log in
    Then the should be successfully logged into the site

  Scenario: User cannot login the trello with invalid email address
    Given A user is on the trello website
    When the user clicks Log in
    And the user enters invalid email <email>
    Then the user is redirected to signup
