"""A collection of classes that check for certain conditions"""

class RolledDownChecker(object):
    """a callable that checks if a hover menu displays an item"""

    def __init__(self, link_text):
        self._link_text = link_text

    def __call__(self, driver):
        item = driver.find_element_by_link_text(self._link_text)
        return item if item.location_once_scrolled_into_view['y'] > 0 else None
