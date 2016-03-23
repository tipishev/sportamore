from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
title_contains = expected_conditions.title_contains

from elements import BasePageElement
from checkers import RolledDownChecker
from locators import BasePageLocators
consumer_menu_locator = BasePageLocators.consumer_menu_locator

TIMEOUT = 5 # seconds

"""These objects abstract methods for interacting with corresponding page types"""

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def go_to_consumer_product_category(self, consumer, product_category):
        """Navigate to consumer type product category, e.g. mens t-shirts"""
        driver = self.driver
        consumer_menu = driver.find_element(*consumer_menu_locator(consumer))
        ActionChains(driver).move_to_element(consumer_menu).perform()
        category_rolled_down = RolledDownChecker(product_category)
        product_category_menu = WebDriverWait(driver, TIMEOUT).until(category_rolled_down)
        ActionChains(driver).click(product_category_menu).perform()
        WebDriverWait(driver, TIMEOUT).until(title_contains(product_category))

class MainPage(BasePage):
    """Main page (sportamore.se)"""

class ConsumerProductCategoryPage(BasePage):
    """Consumer type and product category page, e.g. sportamore.se/dam/klader/jackor/"""

class ProductPage(BasePage):
    """Product page, e.g. https://www.sportamore.se/produkt/89563-blacc-glow-f-rosa"""

class AddToShoppingCartPage(BasePage):
    """Add to shopping cart page (https://www.sportamore.se/cart/add/)"""

