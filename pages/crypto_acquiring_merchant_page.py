import random
import time

import keyboard
import pyperclip

from selenium.webdriver import Keys
from selenium.common import TimeoutException
from selenium.webdriver.chrome import webdriver

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

    def invoices_order_id(self):
        self.element_is_visible(self.locators.INVOICES_BUTTON).click()
        order_id = self.element_is_visible(self.locators.ORDER_ID).text
        self.element_is_visible(self.locators.INVOICE_DETAILS_BUTTON).click()
        order_id_result = self.element_is_visible(self.locators.ORDER_ID_RESULT).text
        time.sleep(1)
        return order_id, order_id_result

    def generate_invoice(self):
        self.element_is_visible(self.locators.INVOICES_BUTTON).click()
        self.element_is_visible(self.locators.GENERATE_INVOICE_BUTTON).click()
        self.element_is_visible(self.locators.INVOICE_AMOUNT_FIELD).send_keys('0.0001')
        self.element_is_visible(self.locators.INVOICE_CURRENCY_BUTTON).click()
        self.element_is_present(self.locators.INVOICE_CURRENCY_FIELD).send_keys('BTC')
        keyboard.send('enter')
        self.element_is_visible(self.locators.GET_INVOICE_URL_BUTTON).click()
        self.element_is_visible(self.locators.COPY_INVOICE_URL_BUTTON).click()
        keyboard.send('Ctrl+t')
        keyboard.send('Ctrl+v')
        keyboard.send('enter')
        time.sleep(2)






