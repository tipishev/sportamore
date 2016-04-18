#!/usr/bin/env python3

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages import (
        MainPage,
        ConsumerProductCategoryPage,
        ProductPage,
        AddToShoppingCartPage
)

from config import log

REMOTE_DRIVER_ENDPOINT = "http://127.0.0.1:4444/wd/hub"
MAIN_PAGE_URL = "https://www.sportamore.se"

class SportamoreTestCase(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Remote(
                command_executor = REMOTE_DRIVER_ENDPOINT,
                desired_capabilities = DesiredCapabilities.FIREFOX,
        )
        self.driver.get(MAIN_PAGE_URL)

    def test_upsell_on_featured_mens_product(self):
        CONSUMER = "Herr"
        PRODUCT_CATEGORY = "Byxor"
        EXPECTED_URL = "https://www.sportamore.se/herr/klader/byxor/"
        EXPECTED_UPSELL = {'Slim 500ml', '3Ppk Value No Show'}

        driver = self.driver

        # navigate from the Main page to "herr/byxor" via hover-menu
        main_page = MainPage(driver)
        main_page.go_to_consumer_product_category(CONSUMER, PRODUCT_CATEGORY)

        # click on the featured product
        consumer_product_category_page = ConsumerProductCategoryPage(driver)
        current_url = consumer_product_category_page.current_url
        self.assertEqual(current_url, EXPECTED_URL)
        consumer_product_category_page.go_to_featured_product()

        # proceed to quantity selection
        product_page = ProductPage(driver)
        # ↓ an abstraction leak to demo flexibility
        product_page.size_select.select_first_size()
        product_page.go_to_add_to_cart()

        # check the actual upsell products against expected
        add_to_cart_page = AddToShoppingCartPage(driver)
        actual_upsell = add_to_cart_page.get_upsell_items()

        self.assertTrue(EXPECTED_UPSELL.issubset(actual_upsell),
                "Unexpected upsell items: {}".format(
                    EXPECTED_UPSELL.difference(actual_upsell)
                )
        )

    def test_upsell_on_featured_womens_product(self):
        CONSUMER = "Dam"
        PRODUCT_CATEGORY = "Underkläder"
        EXPECTED_URL = "https://www.sportamore.se/dam/klader/underklader/"
        EXPECTED_UPSELL = {'Slim 500ml', '3Ppk Value No Show'}

        driver = self.driver

        # navigate from the Main page to "herr/byxor" via hover-menu
        main_page = MainPage(driver)
        main_page.go_to_consumer_product_category(CONSUMER, PRODUCT_CATEGORY)

        # click on the featured product
        consumer_product_category_page = ConsumerProductCategoryPage(driver)
        current_url = consumer_product_category_page.current_url
        self.assertEqual(current_url, EXPECTED_URL)
        consumer_product_category_page.go_to_featured_product()

        # proceed to quantity selection
        product_page = ProductPage(driver)
        # ↓ an abstraction leak to demo flexibility
        product_page.size_select.select_first_size()
        product_page.go_to_add_to_cart()

        # check the actual upsell products against expected
        add_to_cart_page = AddToShoppingCartPage(driver)
        actual_upsell = add_to_cart_page.get_upsell_items()

        self.assertTrue(EXPECTED_UPSELL.issubset(actual_upsell),
                "Unexpected upsell items: {}".format(
                    EXPECTED_UPSELL.difference(actual_upsell)
                )
        )


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
