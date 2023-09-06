import time

from pages.crypto_acquiring_merchant_page import MerchantCabAuth, MerchantCabCryptoAcquiring


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


