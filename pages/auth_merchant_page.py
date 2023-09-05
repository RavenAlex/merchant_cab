import random
import time

import keyboard

from selenium.webdriver import Keys
from selenium.common import TimeoutException

from locators.auth_merchnt_locators import AuthMerchantCabLocators
from pages.base_page import BasePage


class MerchantCabAuth(BasePage):
    locators = AuthMerchantCabLocators()

    def auth_merchant_cab(self):
        self.element_is_visible(self.locators.EMAIL_AUTH).send_keys('agureev@clarus.tech')
        self.element_is_visible(self.locators.PASSWORD_AUTH).send_keys('!WBf7BRBEP')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        login_result = self.element_is_visible(self.locators.LOGIN_RESULT).get_attribute('value')
        return login_result

