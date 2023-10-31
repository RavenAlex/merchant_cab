from selenium.webdriver.common.by import By


class AuthMerchantCabLocators:
    EMAIL_AUTH = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_AUTH = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiButton-root Button_root__2QlEq '
                                     'MuiButton-contained Button_buttonContainer__VXHtH Button_primary__2U6tv"]')
    LOGIN_RESULT = (By.XPATH, '//*[@id="__next"]/div/div/main/header/div/div/div/div/input')
    LOG_OUT_FIELD = (By.XPATH, '//*[@id="__next"]/div/div/main/header/div/div/div/div')
    LOG_OUT_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/header/div/div/div/div[2]')


class MerchantCabCryptoAcquiringLocators:
    EMAIL_AUTH = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_AUTH = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiButton-root Button_root__2QlEq '
                                     'MuiButton-contained Button_buttonContainer__VXHtH Button_primary__2U6tv"]')
    SETTINGS_BUTTON = (By.CSS_SELECTOR, 'a[href="/merchants/crypto-acquiring/settings/"]')
    ADD_CURRENCY_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div[1]/div[1]/section/button')
    ADD_CURRENCY_BUTTON_CONFIRM = (By.XPATH, '/html/body/div[3]/div/div/div/div/button/span[1]')
    CURRENCY_TEXT_AFTER_ADD = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div[1]/div[1]/section/div/span')
    CURRENCY_TEXT = (By.XPATH, '/html/body/div[3]/div/div/div/div')
    CURRENCY_DELETE_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div[1]/div[1]/section/div/span/button')
    CUSTOMERS_ID_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/table/tbody/tr/td[1]')
    CUSTOMERS_ID = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/table/tbody/tr/td[1]/a')
    CUSTOMERS_ID_RESULT = (By.XPATH, '/html/body/div[4]/div/div/h2/span')
    INVOICES_BUTTON = (By.CSS_SELECTOR, 'a[href="/merchants/crypto-acquiring/invoices/"]')
    ORDER_ID = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/table/tbody/tr[1]/td[4]/div')
    INVOICE_DETAILS_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/table/tbody/tr[1]/td['
                                        '7]/button/span[1]')
    ORDER_ID_RESULT = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[4]')
    GENERATE_INVOICE_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/button/span[1]/div[2]')
    INVOICE_ORDER_ID = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[1]/input')
    PAY_FORM_ORDER_ID = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div[1]')
    INVOICE_AMOUNT_FIELD = (By.XPATH, '/html/body/div[4]/div/div/div[3]/div[1]/input')
    INVOICE_CURRENCY_BUTTON = (By.XPATH, '/html/body/div[4]/div/div/div[3]/div[2]/div/div/div')
    INVOICE_CURRENCY_FIELD = (By.XPATH, '//*[@id="react-select-2-input"]')
    GET_INVOICE_URL_BUTTON = (By.XPATH, '/html/body/div[4]/div/div/div[4]/button[1]')
    COPY_INVOICE_URL_BUTTON = (By.XPATH, '/html/body/div[4]/div/div/div[5]/div[2]/div[2]')
    PAYOUTS_BUTTON = (By.CSS_SELECTOR, 'a[href="/merchants/crypto-acquiring/payouts/"]')
    DATE_AND_TIME_OF_PAYOUT = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/table/tbody/tr[1]/td[1]/div')
    PAYOUT_DETAILS_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/table/tbody/tr[1]/td[3]')
    DATE_AND_TIME_OF_PAYOUT_DETAILS = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[1]/div[4]')
    TRANSPORT_SET_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[5]/div')
    TRANSPORT_NEXT_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[6]/button')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    EMAIL_NEXT_BUTTON = (By.CSS_SELECTOR, 'button[class="Button_root__BkQ0y  "]')
    PAY_BUTTON = (By.CSS_SELECTOR, 'button[class="Button_root__BkQ0y  "]')
    CONFIRM_PAY_BUTTON = (By.CSS_SELECTOR, 'a[style="color: green"]')
    REJECT_PAY_BUTTON = (By.CSS_SELECTOR, 'a[style="color: darkred"]')
    STATE_BEFORE_PAY = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]')
    STATE_AFTER_PAY = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[3]/div/div[1]/div/div/div[2]')


class MerchantCabBalanceLocators:
    EMAIL_AUTH = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_AUTH = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiButton-root Button_root__2QlEq '
                                     'MuiButton-contained Button_buttonContainer__VXHtH Button_primary__2U6tv"]')
    BALANCE_BUTTON = (By.CSS_SELECTOR, 'a[href="/merchants/balance/"]')
    BALANCE_STATUS = (By.XPATH, '//div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]')
    WALLETS_STATUS = (By.XPATH, '//div[2]/div[1]/div[2]/div[2]')
    BALANCE_HIDE_BUTTON = (By.XPATH, '//div[1]/span/span[1]')
    WALLETS_HIDE_BUTTON = (By.XPATH, '//div[2]/span/span[1]')
    PAYOUT_DATE = (By.XPATH, '//tr[1]/td[1]/div')
    WITHDRAW_BUTTON = (By.XPATH, '//div/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]')
    CURRENCY_BUTTON = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div')
    CURRENCY_SET = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[4]')
    CURRENCY_AMOUNT = (By.CSS_SELECTOR, 'input[class="Input_input__1qukR WithdrawModal_amountInput__15ck4"]')
    WITHDRAW_SUBMIT_BUTTON = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[3]/button[1]')
    WITHDRAW_STATE = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div')
    WITHDRAW_STATUS = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[7]/div')
    CONVERT_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/button[2]')
    CONVERT_AMOUNT_FIELD = (By.CSS_SELECTOR, 'input[class="Input_input__1qukR"]')
    CONVERT_SUBMIT_BUTTON = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/button[1]/span[1]/div')
    CONVERT_RESULT_TEXT = (By.XPATH, '/html/body/div[5]/div/div/div[2]/div')
    CONVERT_BUTTON_OK = (By.XPATH, '/html/body/div[5]/div/div/div[3]/button/span[1]/div')
    CONVERT_BUTTON_CANCEL = (By.XPATH, '/html/body/div[3]/div/div/div[2]/div[2]/button[2]/span[1]/div')
    TRANSACTION_HISTORY = (By.CSS_SELECTOR, 'a[href="/merchants/transaction-history/"]')
    EXCHANGE_RESULT = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div/table/tbody/tr[1]/td[2]/div')




