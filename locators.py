"""Element locators, scoped by page classes using them"""

from selenium.webdriver.common.by import By
from domain import CONSUMERS

class BasePageLocators(object):
    """Locators common to all pages"""

    @staticmethod
    def consumer_menu_locator(item):
        """Locator for consumer (Herr/Dam/Barn) entry in hover menu"""
        assert item in CONSUMERS, "unknown consumer type"
        return (By.LINK_TEXT, item)

class ConsumerProductCategoryPageLocators(object):
    """Locators specific to Consumer Product Category pages"""
    FEATURED_PRODUCT_LOCATOR = (By.CLASS_NAME, "featured-wrapper")

class ProductPageLocators(object):
    """Locators specific to Product pages"""
    SIZE_SELECT_LOCATOR = (By.XPATH, "//*[@id='buy-form']/select")
    BUY_FORM_LOCATOR = (By.ID, "buy-form")

class AddToShoppingCartPageLocators(object):
    """Locators specific to Add to Shopping Cart"""
    UPSELL_ITEMS_SELECTOR = (By.XPATH, '//*[@id="mp_promoted_row"]/*/article/div[1]/div/a/span')
