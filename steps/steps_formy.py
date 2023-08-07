from behave import*
@when(u'I enter a valid firstname :John')
def step_impl(context):
    print(u'STEP: When I enter a valid firstname :John')


@when(u'I enter a valid lastname: Max')
def step_impl(context):
    print(u'STEP: When I enter a valid lastname: Max')


@when(u'I enter a job title: tester')
def step_impl(context):
    print(u'STEP: When I enter a job title: tester')


@when(u'I check one of the following options on tht  highest level of education: High School, College, Grad School')
def step_impl(context):
    print(u'STEP: When I check one of the following options on tht  highest level of education: High School, College, Grad School')


@when(u'I select one of the following options on Sex: Male, Female, Prefer not to say')
def step_impl(context):
    print(u'STEP: When I select one of the following options on Sex: Male, Female, Prefer not to say')


@when(u'I select  one of the options on years of experience')
def step_impl(context):
    print(u'STEP: When I select  one of the options on years of experience')


@when(u'I select date from the date pick')
def step_impl(context):
    print(u'STEP: When I select date from the date pick')


@when(u'I click on Submit button')
def step_impl(context):
    print(u'STEP: When I click on Submit button')


@then(u'I receive the succes message- The form was successfully submitted!')
def step_impl(context):
    print(u'STEP: Then I receive the succes message- The form was successfully submitted!')


@then(u'I receive the following error message- You need to fill up the job title field')
def step_impl(context):
    print(u'STEP: Then I receive the following error message- You need to fill up the job title field')

