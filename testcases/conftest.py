import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager as ChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function", autouse=True)
def setup(request, browser):
    if "chrome" == browser:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "chromium":
        driver = webdriver.Chrome(service=ChromiumService(ChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help= "Browser to use for tests. Options: chrome, edge, chromium, firefox")


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

