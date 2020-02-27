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

        # She put the values of x and y in the integerfield, click add button and saw her result
        x = self.browser.find_element_by_id('input_1') 
        x.send_keys('5')
        y = self.browser.find_element_by_id('input_2') 
        y.send_keys('3')

        add_button = self.browser.find_element_by_id('add') 
        add_button.click()
        time.sleep(1)
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Result is 8', result_text)
        time.sleep(1)


        # She put the values of x and y in the integerfield, click sub button and saw her result
        x = self.browser.find_element_by_id('input_1') 
        x.send_keys('5')
        y = self.browser.find_element_by_id('input_2') 
        y.send_keys('3')

        sub_button = self.browser.find_element_by_id('sub') 
        sub_button.click()
        time.sleep(1)
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Result is 2', result_text)
        time.sleep(1)


        # She put the values of x and y in the integerfield, click multiple button and saw her result
        x = self.browser.find_element_by_id('input_1') 
        x.send_keys('5')
        y = self.browser.find_element_by_id('input_2') 
        y.send_keys('3')

        multiple_button = self.browser.find_element_by_id('multiple') 
        multiple_button.click()
        time.sleep(1)
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Result is 15', result_text)
        time.sleep(1)



        # She put the values of x and y in the integerfield, click divide button and saw her result
        x = self.browser.find_element_by_id('input_1') 
        x.send_keys('15')
        y = self.browser.find_element_by_id('input_2') 
        y.send_keys('3')

        divide_button = self.browser.find_element_by_id('divide') 
        divide_button.click()
        time.sleep(1)
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Result is 5', result_text)
        time.sleep(1)
        
       
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()