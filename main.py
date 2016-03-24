#!/usr/bin/env python3.4 

import unittest
from selenium import webdriver
from pages import (
        MainPage,
        ConsumerProductCategoryPage,
        ProductPage,
        AddToShoppingCartPage
)


class SportamoreTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()  # TODO: play with remote driver
        self.driver.get("https://www.sportamore.se")

    def test_upsell_on_featured_product(self):
        CONSUMER = "Dam"
        PRODUCT_CATEGORY = "Underkläder"
        EXPECTED_UPSELL_ITEMS = {'Slim 500ml', '3Ppk Value No Show'}

        driver = self.driver

        # navigate from the Main page to "herr/byxor" via hover-menu
        main_page = MainPage(driver)
        main_page.go_to_consumer_product_category(CONSUMER, PRODUCT_CATEGORY)

        # self.assertTrue(driver.current_url.endswith("sportamore.se/herr/byxor/"))
        # self.assertTrue(driver.current_url.endswith("sportamore.se/herr/klader/byxor/"))

        # click on the featured product
        consumer_product_category_page = ConsumerProductCategoryPage(driver)
        consumer_product_category_page.go_to_featured_product()

        # proceed to quantity selection
        product_page = ProductPage(driver)
        # ↓ an abstraction leak to demo flexibility
        product_page.size_select.select_first_size()
        product_page.go_to_add_to_cart()

       # check the actual upsell products against expected

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
