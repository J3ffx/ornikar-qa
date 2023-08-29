Feature: API Testing
  Scenario: Get all todos
    When I make a GET request to "/todos"
    Then the response status code should be 200
    And the response body should contain "Do something nice for someone I care about"

  Scenario: Get a single todo
    When I make a GET request to "/todos/1"
    Then the response status code should be 200
    And the response body should contain "Do something nice for someone I care about"

  Scenario: Limit and skip todos
    When I make a GET request to "/todos?limit=3&skip=10"
    Then the response status code should be 200
    And the response body should contain "Text a friend I haven't talked to in a long time"
    And the response body should contain "Organize pantry"
    And the response body should contain "Buy a new house decoration"

  Scenario: Add a new todo
    When I make a POST request to "/todos/add" with the following JSON payload:
    """
    {
        "todo": "Use Behave for API testing",
        "completed": false,
        "userId": 42
    }
    """
    Then the response status code should be 200
    And the response body should contain "Use Behave for API testing"
