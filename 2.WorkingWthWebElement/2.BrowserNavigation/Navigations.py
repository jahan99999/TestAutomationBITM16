from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class Navigation():
    def browser_navigate(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://www.google.com')

        driver.get('https://www.goal.com')

        # Goes one step backward in the browser history.
        # Back to google
        driver.back()

        # Goes one step forward in the browser history.
        # Forward to GOAL
        driver.forward()

        # Refreshes the current page.
        # Reload the browser
        driver.refresh()

        driver.close()


test_obj = Navigation()
test_obj.browser_navigate()





