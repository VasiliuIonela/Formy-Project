Feature: Test the Login functionality on internet herokuapp
  #https://the-internet.herokuapp.com/login
  Background: I am on the login page on the internet app

  Scenario Outline: We test invalid login combinations for username and password
    When I use invalid <username> or <password>
    And I click the Login  button
    Then I get an error message
    Examples:
      | username | password             |
      | username | SuperSecretPassword! |
      | tomsmith | password             |
      | userna   | password12           |

  Scenario:  check valid login
    When I insert valid username and password
    And I click the Login button
    Then I get the success message  -  You logged into a secure area!

  Scenario: check valid login after removing previews content of the fields
    When I select the text from the username field (duble click or ctrl+a)
    And I press the backspace button
    And I select th text from the password filed(duble click or ctrl+a)
    And I insert valid username and password
    And I press the backspace button
    And I click the Login button
    Then I get the success message    You logged into a secure area!
    

