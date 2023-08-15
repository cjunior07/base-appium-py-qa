import pytest
import os
from pytests.support.screenshot_service import ScreenshotService
from appium import webdriver
from pytests.support.log_service import LogService
LOG = LogService
os.environ['path_screenshot'] = f"{os.getcwd()}\\pytests\\screenshot\\screenshot.png"

@pytest.fixture(scope="session", autouse=True)
def before_all():
    LOG.log_info("---Before All---")
    yield
    LOG.log_info("---After All---")

@pytest.fixture(autouse=True)
def driver():
    options = {
  "platformName": "Android",
  "appium:deviceName": "pixel_3a",
  "appium:app": f"{os.getcwd()}/app/marvelopedia.apk",
  "appium:autoGrantPermissions": True,
  "appium:locationServicesEnabled": True
}
    
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options)
    yield driver
    ScreenshotService.take_screenshot(driver)
    driver.quit