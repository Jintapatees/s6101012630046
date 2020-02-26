from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_calculate_number(self):
        # Linda has heard about a cool new online Calculator app 
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention Calculator
        self.assertIn('Calculator', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Calculator', header_text)

        # She put the values of x and y in the integerfield 
        x = self.browser.find_element_by_id('input_1') 
        x.send_keys('5')

        y = self.browser.find_element_by_id('input_2') 
        y.send_keys('3')

        # And she click add button
        add_button = self.browser.find_element_by_id('add') 
        add_button.click()
        time.sleep(2)

        # She saw her result
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Result is 8', result_text)
        time.sleep(3)
       
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()