import allure
from pytests.support.hooks import *

class ScreenshotService:

    def take_screenshot(driver):
        driver.save_screenshot(os.environ['path_screenshot'])
        allure.attach.file(os.environ['path_screenshot'], attachment_type=allure.attachment_type.PNG)