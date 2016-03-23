from selenium.webdriver.common.by import By
from domain import CONSUMERS

class BasePageLocators(object):
    """Locators common to all pages"""

    @staticmethod
    def consumer_menu_locator(item):
        """Locator for consumer menu"""
        assert item in CONSUMERS, "unknown consumer type"
        return (By.LINK_TEXT, item)

# class SearchResultsPageLocators(object):
#     """A class for search results locators. All search results locators should come here"""
#     pass
