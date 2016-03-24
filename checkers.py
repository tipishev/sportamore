"""A collection of callables that check for certain conditions"""

class RolledDownChecker(object):
    """checks if an item is shown in hover menu"""

    def __init__(self, link_text):
        self._link_text = link_text

    def __call__(self, driver):
        item = driver.find_element_by_link_text(self._link_text)
        return item if item.location_once_scrolled_into_view['y'] > 0 else None

class UrlContainsChecker(object):
    """checks if the URL contains a string"""

    def __init__(self, url_substring):
        self._url_substring = url_substring

    def __call__(self, driver):
        current_url = driver.current_url
        return current_url if self._url_substring in current_url else None
