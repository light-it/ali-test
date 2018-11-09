import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from local_func import env
import page


def init():
    return webdriver.Chrome()


def main(driver):
    driver.get('https://www.aliexpress.com/')

    page.AnyPage(driver).do_escape()
    page.AnyPage(driver).go_to_globalsite()
    time.sleep(2)

    page.MainPage(driver).click_login()

    time.sleep(2)

    login_page = page.LoginPage(driver)
    login_page.goto_login_iframe()
    login_page.enter_credits_and_login(env('ALI_USER'), env('ALI_PASS'))

    time.sleep(3)

    page.AnyPage(driver).do_escape()
    mainpage = page.MainPage(driver)
    mainpage.click_change_ship_curency()
    mainpage.search('Boys Bicycle')

    time.sleep(3)

    search_results = page.SearchResults(driver)
    search_results.click_first()
    search_results.switch_tab(1)

    time.sleep(1)

    driver.save_screenshot('test.png')

    time.sleep(10)

    driver.quit()


if __name__ == '__main__':
    main(init())