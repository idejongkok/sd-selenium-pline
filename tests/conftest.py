import pytest
import allure
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    """
    Initialize Selenium WebDriver using Selenium Grid.
    """

    grid_url = "http://selenium-hub:4444/wd/hub"  # Selenium Grid Hub URL

    with allure.step("Setup Remote WebDriver for Selenium Grid"):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Remote(
            command_executor=grid_url,
            options=options
        )
        driver.implicitly_wait(15)

    try:
        with allure.step("Open Saucedemo URL"):
            driver.get("https://saucedemo.com")

        yield driver

    finally:
        with allure.step("Teardown: Close Browser"):
            driver.quit()
