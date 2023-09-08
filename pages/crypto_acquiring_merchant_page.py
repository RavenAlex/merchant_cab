import random
import time

import keyboard
import pyperclip

from selenium.webdriver import Keys
from selenium.common import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote import switch_to
from webdriver_manager.core import driver

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
        driver = self.driver
        window_before = driver.window_handles[0]
        self.element_is_visible(self.locators.INVOICES_BUTTON).click()
        self.element_is_visible(self.locators.GENERATE_INVOICE_BUTTON).click()
        invoice_order_id = self.element_is_visible(self.locators.INVOICE_ORDER_ID).get_attribute('value')
        self.element_is_visible(self.locators.INVOICE_AMOUNT_FIELD).send_keys('0.0001')
        self.element_is_visible(self.locators.INVOICE_CURRENCY_BUTTON).click()
        self.element_is_present(self.locators.INVOICE_CURRENCY_FIELD).send_keys('BTC')
        keyboard.send('enter')
        self.element_is_visible(self.locators.GET_INVOICE_URL_BUTTON).click()
        self.element_is_visible(self.locators.COPY_INVOICE_URL_BUTTON).click()
        keyboard.send('Ctrl+t')
        keyboard.send('Ctrl+v')
        keyboard.send('enter')
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        pay_form_order_id = self.element_is_present(self.locators.PAY_FORM_ORDER_ID).text.split('№')[1].split('\n')[0]
        return invoice_order_id, pay_form_order_id

    def payout_details(self):
        self.element_is_visible(self.locators.PAYOUTS_BUTTON).click()
        date_and_time_of_payout = self.element_is_visible(self.locators.DATE_AND_TIME_OF_PAYOUT).text
        self.element_is_visible(self.locators.PAYOUT_DETAILS_BUTTON).click()
        date_and_time_of_payout_details = self.element_is_visible(self.locators.DATE_AND_TIME_OF_PAYOUT_DETAILS).text
        return date_and_time_of_payout, date_and_time_of_payout_details

    def invoice_payment(self):
        driver = self.driver
        window_before = driver.window_handles[0]
        self.element_is_visible(self.locators.INVOICES_BUTTON).click()
        self.element_is_visible(self.locators.GENERATE_INVOICE_BUTTON).click()
        self.element_is_visible(self.locators.INVOICE_ORDER_ID).get_attribute('value')
        self.element_is_visible(self.locators.INVOICE_AMOUNT_FIELD).send_keys('0.0001')
        self.element_is_visible(self.locators.INVOICE_CURRENCY_BUTTON).click()
        self.element_is_present(self.locators.INVOICE_CURRENCY_FIELD).send_keys('BTC')
        keyboard.send('enter')
        self.element_is_visible(self.locators.GET_INVOICE_URL_BUTTON).click()
        self.element_is_visible(self.locators.COPY_INVOICE_URL_BUTTON).click()
        keyboard.send('Ctrl+t')
        keyboard.send('Ctrl+v')
        keyboard.send('enter')
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        self.element_is_visible(self.locators.TRANSPORT_SET_BUTTON).click()
        self.element_is_visible(self.locators.TRANSPORT_NEXT_BUTTON).click()
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys('alexandre.gureev@yandex.ru')
        self.element_is_visible(self.locators.EMAIL_NEXT_BUTTON).click()
        time.sleep(2)
        self.element_is_visible(self.locators.PAY_BUTTON).click()
        self.element_is_visible(self.locators.CONFIRM_PAY_BUTTON).click()
        state_before_pay = self.element_is_visible(self.locators.STATE_BEFORE_PAY).text
        time.sleep(400)
        driver.refresh()
        state_after_pay = self.element_is_visible(self.locators.STATE_AFTER_PAY).text
        return state_before_pay, state_after_pay





