from selenium.webdriver.common.by import By


class AuthMerchantCabLocators:
    EMAIL_AUTH = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_AUTH = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiButton-root Button_root__2QlEq '
                                     'MuiButton-contained Button_buttonContainer__VXHtH Button_primary__2U6tv"]')
    LOGIN_RESULT = (By.XPATH, '//*[@id="__next"]/div/div/main/header/div/div/div/div/input')