from selenium.webdriver.common.by import By
from domain import CONSUMERS

class BasePageLocators(object):
    """Locators common to all pages"""

    @staticmethod
    def consumer_menu_locator(item):
        """Locator for consumer menu"""
        assert item in CONSUMERS, "unknown consumer type"
        return (By.LINK_TEXT, item)

class ConsumerProductCategoryPageLocators(object):
    """Locators specific to Consumer Product Category pages"""
    FEATURED_PRODUCT_LOCATOR = (By.CLASS_NAME, "featured-wrapper")
