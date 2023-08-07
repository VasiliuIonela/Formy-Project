import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://pastebin.com/")
        self.driver.implicitly_wait(5)
    def tearDown(self) -> None:
        self.driver.quit()
    '''
        Open https://pastebin.com/ or a similar service in any browser.
    Create 'New Paste' with the following attributes:
    * Code: "Hello from WebDriver"
    * Paste Expiration: "10 Minutes"
    * Paste Name / Title: "helloweb"
    '''
    @unittest.skip
    def test_newPaste(self):
        self.driver.find_element(By.XPATH, "//button[text()='AGREE']").click()
        #self.driver.find_element(By.XPATH, "//a[@class='header__btn']").click()
        self.driver.find_element(By.ID, "postform-text").send_keys("Hello from WebDriver")
        time.sleep(2)
        self.driver.find_element(By.ID, "postform-name").send_keys("helloweb")
        time.sleep(3)
        self.driver.find_element(By.ID, "select2-postform-expiration-container").click()
        time.sleep(5)
        #self.driver.find_element(By.XPATH, "//span[@title='10 Minutes']").is_selected()
        time.sleep(3)
        #assert self.driver.find_element(By.XPATH,"//div[@class='content__title -no-border']").text =='New Paste'
    '''
    Create 'New Paste' with the following attributes:
    * Code:
    git config --global user.name  "New Sheriff in Town"
    git reset $(git commit-tree HEAD^{tree} -m "Legacy code")
    git push origin master --force
    * Syntax Highlighting: "Bash"
    * Paste Expiration: "10 Minutes"
    * Paste Name / Title: "how to gain dominance among developers"
    3. Save 'paste' and check the following:
    * Browser page title matches 'Paste Name / Title'
    * Syntax is suspended for bash
    * Check that the code matches the one from paragraph 2
    '''
    def test_second_paste(self):
        self.driver.find_element(By.XPATH, "//button[text()='AGREE']").click()
        self.driver.find_element(By.ID, "postform-name").send_keys("how to gain dominance among developers")
        self.driver.find_element(By.ID,"select2-postform-format-container").click()
        #self.driver.find_element(By.ID,"select2-postform-format-result-gatk-8").click()
        time.sleep(3)

        time.sleep(3)
        #self.driver.find_element(By.ID, "select2-postform-expiration-container").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//button[text() ='Create New Paste']").click()


    #<li class="select2-results__option select2-results__option--highlighted"
    # id="select2-postform-format-result-gatk-8" role="option" aria-selected="true"
    # data-select2-id="select2-postform-format-result-gatk-8">Bash</li>
//div[@class='pdp-action-item-header__checkbox--unchecked' and contains(text()= 'Step 1. Set the direction for self-development')]
