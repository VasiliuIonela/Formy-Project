Feature: Test submission on formy project
  # https://formy-project.herokuapp.com/form
  Background: I am on the formy project page
  Scenario: submit the form with valid data in all fields
    When I enter a valid firstname :John
    And I enter a valid lastname: Max
    And I enter a job title: tester
    And I check one of the following options on tht  highest level of education: High School, College, Grad School
    And I select one of the following options on Sex: Male, Female, Prefer not to say
    And I select  one of the options on years of experience
    And I select date from the date pick
    And I click on Submit button
    Then I receive the succes message- The form was successfully submitted!

  Scenario: submit the form without filling up the job title field
    When I enter a valid firstname :John
    And I enter a valid lastname: Max
    And I check one of the following options on tht  highest level of education: High School, College, Grad School
    And I select one of the following options on Sex: Male, Female, Prefer not to say
    And I select  one of the options on years of experience
    And I select date from the date pick
    And I click on Submit button
    Then I receive the following error message- You need to fill up the job title field


