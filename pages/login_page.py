    from locators.LoginLocator import LoginLocators
    from core.Base_Page import BasePage
    from config.config import BASE_URL, Headless, timeout
    from core.logger import get_logger


    class LoginPage(BasePage):
        def open_website(self):
            self.navigate(BASE_URL)

        def Login(self, username, password):
            self.fill(LoginLocators.USERNAME, username)
            self.fill(LoginLocators.PASSWORD, password)
            self.click(LoginLocators.LOGIN_BTN)

        def get_inventory_text(self):
            return self.get_text(LoginLocators.INVENTORY_TITLE)

        logger = get_logger()

        logger.info("Logging into application")


