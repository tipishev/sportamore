from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


""" These objects abstract methods for interacting with corresponding page types """

class MainPage(BasePage):
    """Main page (sportamore.se)"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class EndUserProductCategoryPage(BasePage):
    """End user type and product category page, e.g. sportamore.se/dam/klader/jackor/"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source


class ProductPage(BasePage):
    """Product page, e.g. https://www.sportamore.se/produkt/89563-blacc-glow-f-rosa"""

class AddToShoppingCartPage(BasePage):
    """Add to shopping cart page (https://www.sportamore.se/cart/add/)"""

