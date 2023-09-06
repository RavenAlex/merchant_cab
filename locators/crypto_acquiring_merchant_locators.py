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
    ADD_CURRENCY_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div[1]/div['
                                     '6]/section/button/span[1]/div')
    ADD_CURRENCY_BUTTON_CONFIRM = (By.XPATH, '/html/body/div[3]/div/div/div/div[4]/button')
    CURRENCY_TEXT_AFTER_ADD = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div[1]/div['
                                         '6]/section/div/span')
    CURRENCY_TEXT = (By.XPATH, '/html/body/div[3]/div/div/div/div[4]')
    CURRENCY_DELETE_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div[1]/div['
                                        '6]/section/div/span/button')