from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver):
        self.driver = driver
    
    def _visit(self, url):
        self.driver.get(url)

    def _locate(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _click(self, locator):
        self._locate(locator).click()

    def _input(self, locator, input):
        self._locate(locator).send_keys(input)

    def _wait_until_displayed(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((locator["by"], locator["value"])))
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator["by"], locator["value"]))

