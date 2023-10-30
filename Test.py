import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.get("http://skleptest.pl/")

    def test_example(self):
        driver = self.driver
        self.driver.maximize_window()
        elem = self.driver.find_element(By.CSS_SELECTOR, "a[title='Contact']")
        elem.click()
        #elem.send_keys("TEST")

        assert "Contact – Generic Shop" in self.driver.title

        myName = self.driver.find_element(By.CSS_SELECTOR, "input[name='your-name']")
        myName.send_keys("Karol")

        myEmail = self.driver.find_element(By.CSS_SELECTOR, "input[name='your-email']")
        myEmail.send_keys("karol.lukasz.kania@gmail.com")

        mySubject = self.driver.find_element(By.CSS_SELECTOR, "input[name='your-subject']")
        mySubject.send_keys("Pozdrowienia!")

        myMessage = self.driver.find_element(By.CSS_SELECTOR, "textarea[name='your-message']")
        myMessage.send_keys("Pozdrawiam!")

        time.sleep(2)

        btn = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        btn.click()
        time.sleep(5)

        # assert "Thank you for your message. It has been sent." in self.driver.find_element(By.CSS_SELECTOR, '.wpcf7-mail-sent-ok')
        assert self.driver.find_element(By.CSS_SELECTOR, '.wpcf7-mail-sent-ok').is_displayed(), "There is no alert"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
