"""Page elements with specific business logic"""

from selenium.webdriver.support.ui import Select

class SizeSelect(Select):
    """A wrapper for product size selector"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def select_first_size(self):
        """Selects the first size available"""
        first_size = self.options[1].text  # because 0th is "Välj storlek"
        self.select_by_visible_text(first_size)

    def select_smallest(self):
        """Selects the smallest size"""
        self.select_first_size()  # may improve with domain knowledge (XS, S)
