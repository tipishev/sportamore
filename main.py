#!/usr/bin/env python3.4 

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from pages import MainPage, ConsumerProductCategoryPage, ProductPage


class SportamoreTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()  # TODO: play with remote driver
        self.driver.get("https://www.sportamore.se")

    def test_upsell_on_featured_product(self):
        CONSUMER = "Dam"
        PRODUCT_CATEGORY = "Underkläder"
        UPSELL_ITEMS = {'Slim 500ml', '3Ppk Value No Show'}

        driver = self.driver

        main_page = MainPage(driver)
        main_page.go_to_consumer_product_category(CONSUMER, PRODUCT_CATEGORY)

        consumer_product_category_page = ConsumerProductCategoryPage(driver)
        consumer_product_category_page.click_on_featured_product()

        product_page = ProductPage(driver)
        # self.assertTrue(driver.current_url.endswith("sportamore.se/herr/byxor/"))
        # self.assertTrue(driver.current_url.endswith("sportamore.se/herr/klader/byxor/"))



        # time.sleep(1) # FIXME
        # buy_form = driver.find_element_by_id("buy-form")
        # time.sleep(1) # FIXME
        # size_select = Select(buy_form.find_element_by_name("variant_id"))

        # # size_select = Select(WebDriverWait(driver, TIMEOUT).until(
        #     # EC.presence_of_element_located((By.NAME, "variant_id"))))

        # size_select.select_by_visible_text(size_select.options[1].text)
        # buy_form = driver.find_element_by_id("buy-form")
        # buy_form.submit()
        # time.sleep(1)
        # upsell_items = driver.find_element_by_id("mp_promoted_row")
        # links = upsell_items.find_elements_by_tag_name("a")
        # link_texts = set(link.text for link in links if link.text)
        # expected_link_texts = set(['Slim 500ml', '3Ppk Value No Show'])
        # self.assertTrue(expected_link_texts.issubset(link_texts),
        #         "The expected upsell products {} are not present in {}".format(
        #             expected_link_texts, link_texts)
        #         )

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
