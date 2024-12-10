from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, by, locator):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def send_keys_to_element(self, by, locator, keys):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, locator))
        )
        element.clear()
        element.send_keys(keys)

    def find_elements(self, by, value):

        return self.driver.find_elements(by, value)


    def wait_for_element(self, by, locator, timeout=10):

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def scroll_to_element(self, by, value):

        element = self.wait.until(EC.presence_of_element_located((by, value)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_questions(self, locator):

        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def get_current_url(self):
        return self.driver.current_url


    def switch_to_new_window(self, locator):

        self.driver.switch_to.window(self.driver.window_handles[1])


    def wait_for_url_to_be(self, url, timeout=10):

        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))