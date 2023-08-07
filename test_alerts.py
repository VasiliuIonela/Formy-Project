import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAlerts(unittest.TestCase):
    JS_ALERT_LOCATOR = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    JS_MESSAGE = (By.CSS_SELECTOR, "#result")
    #JS_MESSAGE =(By.ID, 'result')
    JS_CONIRFM= (By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    JS_PROMPT = (By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    CONTEXT_SELECTOR = (By.ID, "hot-spot")

    def setUp(self):
        # ruleaza inainte de fiecare test
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.implicitly_wait(5)
        # time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_js_alert(self):
        self.driver.find_element(*self.JS_ALERT_LOCATOR).click()
        self.driver.switch_to.alert.accept()
        assert self.driver.find_element(*self.JS_MESSAGE).text == 'You successfully clicked an alert'

    def test_js_cancel(self):
        self.driver.find_element(*self.JS_CONIRFM).click()
        self.driver.switch_to.alert.dismiss()
        assert self.driver.find_element(*self.JS_MESSAGE).text == "You clicked: Cancel"
    def test_js_prompt(self):
        text = 'acesta este un mesaj de alerta'
        self.driver.find_element(*self.JS_PROMPT).click()
        self.driver.switch_to.alert.send_keys(text)
        self.driver.switch_to.alert.accept()
        self.assertEqual(self.driver.find_element(*self.JS_MESSAGE).text, f'You entered: {text}')

    def test_alert_from_context_menu(self):

        self.driver.get("https://the-internet.herokuapp.com/context_menu")
        ac = ActionChains(self.driver)
        element = self.driver.find_element(*self.CONTEXT_SELECTOR)
        ac.context_click(element).perform() # click dreapta
        self.driver.switch_to.alert.accept()
