import time

from pages.crypto_acquiring_merchant_page import MerchantCabAuth, MerchantCabCryptoAcquiring, \
    MerchantCabBalance


class TestMerchant:
    class TestMerchantAuth:

        def test_auth_and_log_out_merchant(self, driver):
            test_authorization_form = MerchantCabAuth(driver, 'https://int.nimera.io/merchants/login/')
            test_authorization_form.open()
            login_result = test_authorization_form.auth_and_log_out_merchant_cab()
            assert login_result == 'agureev@clarus.tech', 'Login in merchant cab has not been correct work'

    class TestCryptoAcquiring:

        def test_add_and_delete_used_currency(self, driver):
            test_crypto_acquiring = MerchantCabCryptoAcquiring(driver, 'https://int.nimera.io/merchants/login/')
            test_crypto_acquiring.open()
            test_crypto_acquiring.auth_merchant_cab()
            currency, currency_result = test_crypto_acquiring.add_and_delete_used_currency()
            assert currency == currency_result, 'Currency has not been add'

        def test_customers_id(self, driver):
            test_crypto_acquiring = MerchantCabCryptoAcquiring(driver, 'https://int.nimera.io/merchants/login/')
            test_crypto_acquiring.open()
            test_crypto_acquiring.auth_merchant_cab()
            customers_id, customers_id_result = test_crypto_acquiring.customers_id_check()
            assert customers_id == customers_id_result, 'Customers ID not correct'

        def test_invoices_order_id(self, driver):
            test_crypto_acquiring = MerchantCabCryptoAcquiring(driver, 'https://int.nimera.io/merchants/login/')
            test_crypto_acquiring.open()
            test_crypto_acquiring.auth_merchant_cab()
            order_id, order_id_result = test_crypto_acquiring.invoices_order_id()
            assert order_id == order_id_result, 'Invoices details has not been correct work'

        def test_generate_invoice(self, driver):
            test_crypto_acquiring = MerchantCabCryptoAcquiring(driver, 'https://int.nimera.io/merchants/login/')
            test_crypto_acquiring.open()
            test_crypto_acquiring.auth_merchant_cab()
            invoice_order_id, pay_form_order_id = test_crypto_acquiring.generate_invoice()
            assert invoice_order_id == pay_form_order_id, 'Generate invoice has not been correct work'

        def test_payout_details(self, driver):
            test_crypto_acquiring = MerchantCabCryptoAcquiring(driver, 'https://int.nimera.io/merchants/login/')
            test_crypto_acquiring.open()
            test_crypto_acquiring.auth_merchant_cab()
            date_and_time_of_payout, date_and_time_of_payout_details = test_crypto_acquiring.payout_details()
            assert date_and_time_of_payout == date_and_time_of_payout_details, 'Payout details has not been correct ' \
                                                                               'work '

        def test_invoice_payment(self, driver):
            test_crypto_acquiring = MerchantCabCryptoAcquiring(driver, 'https://int.nimera.io/merchants/login/')
            test_crypto_acquiring.open()
            test_crypto_acquiring.auth_merchant_cab()
            state_before_pay, state_after_pay = test_crypto_acquiring.invoice_payment()
            assert state_before_pay == 'Awaiting confirmation' and state_after_pay == 'Confirmed', 'Invoice payment ' \
                                                                                                   'has not been correct work '

    class TestBalance:

        def test_hide_balance_and_wallets(self, driver):
            test_balance = MerchantCabBalance(driver, 'https://int.nimera.io/merchants/login/')
            test_balance.open()
            test_balance.auth_merchant_cab()
            balance_status_before, wallets_status_before, balance_status_after, \
            wallets_status_after = test_balance.check_hide_balance_and_wallets()
            assert balance_status_before != balance_status_after and wallets_status_before != wallets_status_after, \
                'Hide balance or wallet has not been correct work'

        def test_withdraw_from_balance(self, driver):
            test_balance = MerchantCabBalance(driver, 'https://int.nimera.io/merchants/login/')
            test_balance.open()
            test_balance.auth_merchant_cab()
            payout_date_before, withdraw_state, payout_date_after = test_balance.check_withdraw_from_balance()
            assert payout_date_before != payout_date_after and withdraw_state == 'The request has been successfully ' \
                                                                                 'created', 'Withdraw from balance ' \
                                                                                             'hos not been correct ' \
                                                                                             'work '

