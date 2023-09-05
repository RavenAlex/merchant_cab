from datetime import datetime

import allure
import pytest
from selenium import webdriver
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # driver = driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()