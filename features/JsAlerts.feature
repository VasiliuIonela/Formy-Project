Feature:Test javascript alerts cases
  # https://the-internet.herokuapp.com/javascript_alerts
  #Background: I am on the javascript alerts page
  @JsAlert
  Scenario: check js alert
    Given I am on javascript salert page
    When I click on js alert button
    And I accept the js alert
    Then I get the following result message- You successfully clicked an alert
  @JsConfirm
  Scenario: check js confirm
    Given I am on javascript alerts page
    When i click on js confirm button
    And I cancel the js confirm
    Then I get the following result message- You clicked: Cancel

  Scenario: check js prompt
    Given I am on javascripts alerts page
    When I click on js prompt button
    And I insert the message- Hello
    And I click ok on the js prompt
    Then I get the following result message- You entered: Hello






