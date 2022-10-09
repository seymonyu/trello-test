# trello-test

## Purpose

This project is created to test [Trello](https://trello.com/) web app. 
The project contains the test cases for the [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations of trello web application. 

## Setup

This project uses Python 3. The tests are written using [BDD](https://automationpanda.com/bdd/). The tests are written in [Python](https://www.python.org/) using the [pytest-bdd](https://pypi.org/project/pytest-bdd/) library. The required dependencies are listed in requirements.txt file on the root of the repository. The UI tests use the [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) and the default browser used for the tests is [chrome browser](https://www.google.com/intl/tr/chrome/). 

## Features

The object of the test set are the following features; boards, cards, lists. Both API and UI tests are going to be performed for these features. Additionally in UI tests the login feature is briefly covered. 

Every feature and scenario is tagged according to coverage area.

## Test Execution

The tests can be run by running the pytest command on the project root. All the standard options for [pytest command line](https://docs.pytest.org/en/7.1.x/how-to/usage.html) work for filtering etc. 
