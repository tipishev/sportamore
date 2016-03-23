#!/usr/bin/env python3.4 

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

import page

TIMEOUT = 5 # seconds

class RolledDownChecker(object):
    """a callable that checks if a hover menu displays an item"""

    def __init__(self, link_text):
        self._link_text = link_text

    def __call__(self, driver):
        item = driver.find_element_by_link_text(self._link_text)
        return item if item.location_once_scrolled_into_view['y'] > 0 else None

class SportamoreTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_upsell_on_featured_product(self):
        driver = self.driver
        driver.get("https://www.sportamore.se")
        herr = driver.find_element_by_link_text("Herr")
        ActionChains(driver).move_to_element(herr).perform()
        is_byxor_rolled_down = RolledDownChecker("Byxor")
        byxor = WebDriverWait(driver, TIMEOUT).until(is_byxor_rolled_down)
        ActionChains(driver).click(byxor).perform()
        WebDriverWait(driver, TIMEOUT).until(EC.title_contains("Byxor"))
        # self.assertTrue(driver.current_url.endswith("sportamore.se/herr/byxor/"))
        self.assertTrue(driver.current_url.endswith("sportamore.se/herr/klader/byxor/"))
        featured_product = driver.find_element_by_class_name("featured-wrapper")
        ActionChains(driver).click(featured_product).perform()

        time.sleep(1) # FIXME
        buy_form = driver.find_element_by_id("buy-form")
        time.sleep(1) # FIXME
        size_select = Select(buy_form.find_element_by_name("variant_id"))

        # size_select = Select(WebDriverWait(driver, TIMEOUT).until(
            # EC.presence_of_element_located((By.NAME, "variant_id"))))

        size_select.select_by_visible_text(size_select.options[1].text)
        buy_form = driver.find_element_by_id("buy-form")
        buy_form.submit()
        time.sleep(1)
        upsell_items = driver.find_element_by_id("mp_promoted_row")
        links = upsell_items.find_elements_by_tag_name("a")
        link_texts = set(link.text for link in links if link.text)
        expected_link_texts = set(['Slim 500ml', '3Ppk Value No Show', 'Running sock 2-pack'])
        self.assertTrue(expected_link_texts.issubset(link_texts))

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
