from behave import *
@when(u'I use invalid username or SuperSecretPassword!')
def step_impl(context):
    print(u'STEP: When I use invalid username or SuperSecretPassword!')


@when(u'I click the Login  button')
def step_impl(context):
    print(u'STEP: When I click the Login  button')


@then(u'I get an error message')
def step_impl(context):
    print(u'STEP: Then I get an error message')


@when(u'I use invalid tomsmith or password')
def step_impl(context):
    print(u'STEP: When I use invalid tomsmith or password')


@when(u'I use invalid userna or password12')
def step_impl(context):
    print(u'STEP: When I use invalid userna or password12')
    
@when(u'I insert valid username and password')
def step_impl(context):
    print(u'STEP: When I insert valid username and password')


@when(u'I click the Login button')
def step_impl(context):
    print(u'STEP: When I click the Login button')


@then(u'I get the success message    You logged into a secure area!')
def step_impl(context):
    print(u'STEP: Then I get the success message    You logged into a secure area!')


@when(u'I select the text from the username field (duble click or ctrl+a)')
def step_impl(context):
    print(u'STEP: When I select the text from the username field (duble click or ctrl+a)')


@when(u'I press the backspace button')
def step_impl(context):
    print(u'STEP: When I press the backspace button')


@when(u'I select th text from the password filed(duble click or ctrl+a)')
def step_impl(context):
    print(u'STEP: When I select th text from the password filed(duble click or ctrl+a)')

