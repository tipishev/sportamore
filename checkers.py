"""Callables that check for certain events to happen"""

class RolledDown(object):
    """Checks that a link with given text is shown in hover menu"""

    def __init__(self, link_text):
        self._link_text = link_text

    def __call__(self, driver):
        item = driver.find_element_by_link_text(self._link_text)
        return item if item.location_once_scrolled_into_view['y'] > 3 else None

class UrlChanged(object):
    """Checks that the URL has changed since initialization"""

    def __init__(self, driver):
        self.initial_url = driver.current_url

    def __call__(self, driver):
        current_url = driver.current_url
        return current_url if self.initial_url != current_url else None
