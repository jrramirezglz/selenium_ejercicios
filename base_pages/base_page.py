from itertools import dropwhile

import pytest
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self,locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def typte_text(self, locator, text):
        elemento = self.wait_for_element(locator)
        #eliminar el texto que pueda existir
        elemento.clear()
        elemento.send_keys(text)

    def selec_from_dropdown_by_visible_text(self, locator, text):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(text)

    def get_select_option(self, locator):
        dropdown = Select(self.wait_for_element(locator))
        return [option.text for option in dropdown.options]

    def selec_from_dropdown_by_index(self, locator, index):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_index(index)

    def select_element(self, locator):
        element = self.wait_for_element(locator)
        if not element.is_selected():
            element.click()

    def unselect_checkbox(self, locator):
        checkbox = self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()

    def hover_over_element(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def reload_page(self):
        self.driver.refresh()