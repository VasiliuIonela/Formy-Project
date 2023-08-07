import unittest

from selenium import webdriver
from selenium.common import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.common import ElementNotInteractableException
import time
class Elefant(unittest.TestCase):
    COOKIE_SELECTOR = (By.CSS_SELECTOR, "button#CybotCookiesbotDialogBodyLevelButtonLevelOptionAllowAll")
    CLOSE_SELECTOR = (By.CSS_SELECTOR, "button.close")
    MOBILE_LOGO = (By.CSS_SELECTOR, 'a.mobile-logo')
    SEARCH_BAR_SELECTOR= (By.CSS_SELECTOR,'[placeholder= "Căutați cuvânt cheie, codul de produs, tip produs"]')
    SEARCH_NAME =(By.XPATH, "//button[@name='search']")
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(4)
        self.driver.implicitly_wait(3)
        self.driver.get('https://www.elefant.ro/')
        self.driver.maximize_window()
        try:
            self.driver.find_element(*self.COOKIE_SELECTOR).click()
        except NoSuchElementException:
            pass
    def tearDown(self) -> None:
        self.driver.quit()
    def test_elefant_ro(self):
        try:
            self.driver.find_element(*self.CLOSE_SELECTOR).click()
        except ElementNotInteractableException:
            pass
        try:
            self.driver.find_element(*self.MOBILE_LOGO)
        except NoSuchElementException:
            assert False, 'Elementul nu a fost gasit'
    def test_search_bar(self):
        self.driver.implicitly_wait(4)
        self.driver.find_element(*self.SEARCH_BAR_SELECTOR).send_keys('Carti')
        self.driver.find_element(By.XPATH, "//button[@name='search']").is_selected()
        items_list = self.driver.find_elements(By.CSS_SELECTOR, '[class=\'product-title\']')
        assert len(items_list) >= 5, f'Lungimea listei este de {len(items_list)}'
        print('Test search bar passed')

    # def test_title(self):
    #     assert self.driver.title==''

    def test_login_wrong_credentials(self):
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, "//span[text()='Cont']").click()
        self.driver.find_element(By.CSS_SELECTOR, "a.my-account-login").click()
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Email"]').send_keys('abc@.gmail.com')
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Parola"]').send_keys('12345')
        self.driver.find_element(By.NAME, 'login').click()













