import os
from selenium import webdriver
import unittest

class DriverManager(unittest.TestCase):

    @classmethod
    def __init__(self):
        getdir = os.getcwd().split("/")
        getdir.pop()
        self.driver = webdriver.Chrome(executable_path= "/".join(getdir) + "/Drivers/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")
