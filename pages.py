from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select

from elements import SizeSelect
from checkers import RolledDown, UrlChanged
from locators import (BasePageLocators,
                      ConsumerProductCategoryPageLocators,
                      ProductPageLocators)
consumer_menu_locator = BasePageLocators.consumer_menu_locator
featured_product_locator = ConsumerProductCategoryPageLocators.FEATURED_PRODUCT_LOCATOR
size_select_locator = ProductPageLocators.SIZE_SELECT_LOCATOR
buy_form_locator = ProductPageLocators.BUY_FORM_LOCATOR

TIMEOUT = 7 # seconds

"""These objects abstract methods for interacting with corresponding page types"""

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.get_current_url()

    def wait_for_url_change(self):
        WebDriverWait(self.driver, TIMEOUT).until(UrlChanged(self.driver))

    def go_to_consumer_product_category(self, consumer, product_category):
        """Navigate to consumer type product category, e.g. mens t-shirts"""
        driver = self.driver
        consumer_menu = driver.find_element(*consumer_menu_locator(consumer))
        ActionChains(driver).move_to_element(consumer_menu).perform()
        category_rolled_down = RolledDown(product_category)
        product_category_menu = WebDriverWait(driver, TIMEOUT).until(category_rolled_down)
        ActionChains(driver).click(product_category_menu).perform()
        self.wait_for_url_change()

class MainPage(BasePage):
    """Main page (sportamore.se)"""

class ConsumerProductCategoryPage(BasePage):
    """Consumer type and product category page, e.g. sportamore.se/dam/klader/jackor/"""
    def go_to_featured_product(self):
        driver = self.driver
        featured_product = driver.find_element(*featured_product_locator)
        ActionChains(driver).click(featured_product).perform()
        self.wait_for_url_change()

class ProductPage(BasePage):
    """Product page, e.g. https://www.sportamore.se/produkt/89563-blacc-glow-f-rosa"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_select = SizeSelect(
                self.driver.find_element(*size_select_locator))

    def go_to_add_to_cart(self):
        driver = self.driver
        driver.find_element(*buy_form_locator).submit()
        self.wait_for_url_change()

class AddToShoppingCartPage(BasePage):
    """Add to shopping cart page (https://www.sportamore.se/cart/add/)"""
