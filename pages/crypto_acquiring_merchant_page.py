import random
import time

import keyboard

from selenium.webdriver import Keys
from selenium.common import TimeoutException

from locators.crypto_acquiring_merchant_locators import AuthMerchantCabLocators, MerchantCabCryptoAcquiringLocators
from pages.base_page import BasePage


class MerchantCabAuth(BasePage):
    locators = AuthMerchantCabLocators()

    def auth_and_log_out_merchant_cab(self):
        self.element_is_visible(self.locators.EMAIL_AUTH).send_keys('agureev@clarus.tech')
        self.element_is_visible(self.locators.PASSWORD_AUTH).send_keys('!WBf7BRBEP')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        login_result = self.element_is_visible(self.locators.LOGIN_RESULT).get_attribute('value')
        self.element_is_visible(self.locators.LOG_OUT_FIELD).click()
        self.element_is_visible(self.locators.LOG_OUT_BUTTON).click()
        return login_result


class MerchantCabCryptoAcquiring(BasePage):
    locators = MerchantCabCryptoAcquiringLocators()

    def auth_merchant_cab(self):
        self.element_is_visible(self.locators.EMAIL_AUTH).send_keys('agureev@clarus.tech')
        self.element_is_visible(self.locators.PASSWORD_AUTH).send_keys('!WBf7BRBEP')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()

    def add_and_delete_used_currency(self):
        self.element_is_visible(self.locators.SETTINGS_BUTTON).click()
        self.element_is_visible(self.locators.ADD_CURRENCY_BUTTON).click()
        currency = self.element_is_visible(self.locators.CURRENCY_TEXT).text.split('\n')[0]
        self.element_is_visible(self.locators.ADD_CURRENCY_BUTTON_CONFIRM).click()
        currency_result = self.element_is_visible(self.locators.CURRENCY_TEXT_AFTER_ADD).text
        self.element_is_visible(self.locators.CURRENCY_DELETE_BUTTON).click()
        return currency, currency_result

    def customers_id_check(self):
        customers_id = self.element_is_visible(self.locators.CUSTOMERS_ID_BUTTON).text
        self.element_is_visible(self.locators.CUSTOMERS_ID_BUTTON).click()
        customers_id_result = self.element_is_visible(self.locators.CUSTOMERS_ID).text
        return customers_id, customers_id_result



