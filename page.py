import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def _click_css(self, css):
        elem = self.driver.find_element_by_css_selector(css)
        elem.click()

    def switch_tab(self, number=0):
        self.driver.switch_to.window(self.driver.window_handles[number])


class AnyPage(BasePage):
    def do_escape(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def go_to_globalsite(self):
        try:
            self._click_css('[data-role="goto-globalsite"]')
        except NoSuchElementException:
            return
        self.do_escape()


class MainPage(BasePage):
    def click_login(self):
        # if width < 1100
        self.driver.set_window_size(1280, 720)

        login_obj = self.driver.find_element_by_css_selector(
            'a[data-role="sign-link"]',
        )
        login_obj.click()

    def click_change_ship_curency(self):
        switcher_info = self.driver.find_element_by_id('switcher-info')
        switcher_info.click()

        time.sleep(1)

        self._click_css('[data-role="switch-country"]')
        self._click_css('span.css_flag.css_uk')

        self._click_css('[data-role="switch-currency"]')
        self._click_css('[data-currency="GBP"]')

        self._click_css('[data-role="save"]')

    def search(self, query):
        search_obj = self.driver.find_element_by_id('search-key')
        search_obj.click()
        search_obj.send_keys(query)
        search_obj.send_keys(Keys.ENTER)


class SearchResults(BasePage):
    def click_first(self):
        self._click_css(
            '#hs-below-list-items > .list-item:first-child a.product'
        )


class LoginPage(BasePage):
    def goto_login_iframe(self, stepcount=100):
        while (self.driver.switch_to_active_element().tag_name != 'iframe') \
                and (stepcount > 0):
            ActionChains(self.driver).send_keys(Keys.TAB).perform()
            stepcount -= 1

    def enter_credits_and_login(self, login, password):
        actions = ActionChains(self.driver)
        actions.send_keys(login)
        actions.send_keys(Keys.TAB)
        actions.send_keys(password)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
