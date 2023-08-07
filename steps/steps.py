from behave import *
@given(u'I am on javascript salert page')

#@when(u'I click on js alert button')
def step_impl(context):
    print(u'STEP: When I click on js alert button')


@when(u'I accept the js alert')
def step_impl(context):
    print(u'STEP: When I accept the js alert')


@then(u'I get the following result message- You successfully clicked an alert')
def step_impl(context):
    print(u'STEP: Then I get the following result message- You successfully clicked an alert')


@when(u'i click on js confirm button')
def step_impl(context):
    print(u'STEP: When i click on js confirm button')


@when(u'I cancel the js confirm')
def step_impl(context):
    print(u'STEP: When I cancel the js confirm')


@then(u'I get the following result message- You clicked: Cancel')
def step_impl(context):
    print(u'STEP: Then I get the following result message- You clicked: Cancel')


@when(u'I click on js prompt button')
def step_impl(context):
    print(u'STEP: When I click on js prompt button')


@when(u'I insert the message- Hello')
def step_impl(context):
    print(u'STEP: When I insert the message- Hello')


@when(u'I click ok on the js prompt')
def step_impl(context):
    print(u'STEP: When I click ok on the js prompt')


@then(u'I get the following result message- You entered: Hello')
def step_impl(context):
    print(u'STEP: Then I get the following result message- You entered: Hello')
