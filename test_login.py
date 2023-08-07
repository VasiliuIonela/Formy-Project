import time
import unittest
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin(unittest.TestCase):
    USERNAME = "tomsmith"
    PASSWORD = "SuperSecretPassword!"
    WRONG_PASSWORD = "Altceva"
    WRONG_USERNAME = "madalina"
    # definim selectorii de care avem nevoie pentru crearea testelor, care vor fi constante
    USERNAME_SELECTOR = (By.ID, "username")
    PASSWORD_SELECTOR = (By.ID, "password")
    LOGIN_SELECTOR = (By.XPATH, "//button")
    ERROR_MESSAGE = (By.ID, 'flash')
    SUCCESS_MESSAGE = (By.ID, 'flash')
    LOGOUT_SELECTOR = (By.CSS_SELECTOR, "i[class='icon-2x icon-signout']")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")

    @unittest.skip
    def test_invalid_user(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.WRONG_USERNAME)
        time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD)
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        #assert self.driver.find_element(*self.ERROR_MESSAGE).get_attribute('class') == 'flash error'
        #tema verificati mesajul de eroare primit cand se introduce un  username gresit
        assert self.driver.find_element(*self.ERROR_MESSAGE).text == "Your username is invalid!\n×"
        #   sau
        assert "Your username is invalid" in self.driver.find_element(*self.ERROR_MESSAGE).text

    @unittest.skip
    def test_invalid_password(self):
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located((self.USERNAME_SELECTOR)))
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located((By.ID,'password')))
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.WRONG_PASSWORD)
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located(self.LOGIN_SELECTOR))
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        assert self.driver.find_element(*self.ERROR_MESSAGE).text == "Your password is invalid!\n×"
    @unittest.skip
    def test_login_blank_fields(self):
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        assert self.driver.find_element(*self.ERROR_MESSAGE).text == "Your username is invalid!\n×"
    def test_login_corect(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD)
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        #assert self.driver.find_element(*self.ERROR_MESSAGE).text == "You logged into a secure area!\n×"
        self.assertTrue(self.driver.find_element(*self.ERROR_MESSAGE).text == "You logged into a secure area!\n×")
    def test_logout(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD)
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        self.driver.find_element(*self.LOGOUT_SELECTOR).click()
        self.assertEqual(self.driver.find_element(*self.ERROR_MESSAGE).text, f'You logged out of the secure area!\n×')
        #assert self.driver.find_element(*self.ERROR_MESSAGE).text =="You  out of the secure area!\n×"




