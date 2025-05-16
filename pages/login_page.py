from locators.web_locators import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self, username, password):
        self.driver.find_element(*LoginLocators.username_field).send_keys(username)
        self.driver.find_element(*LoginLocators.password_field).send_keys(password)

    def login(self):
        self.driver.find_element(*LoginLocators.login_button).click()

    def is_error_displayed(self):
        return self.driver.find_element(*LoginLocators.error_msg).is_displayed()
