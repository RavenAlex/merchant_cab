from pages.auth_merchant_page import MerchantCabAuth


class TestMerchant:
    class TestMerchantAuth:

        def test_auth_merchant(self, driver):
            test_authorization_form = MerchantCabAuth(driver, 'https://int.nimera.io/merchants/login/')
            test_authorization_form.open()
            login_result = test_authorization_form.auth_merchant_cab()
            assert login_result == 'agureev@clarus.tech', 'Login in merchant cab has not been correct work'
