from pytests.support.hooks import *
from pytests.pages.login_page import LoginPage
import allure

@pytest.mark.test_login_sucesso
def test_login(driver):
    with allure.step("acessar o app"):
        LoginPage.login_screen(driver)
    with allure.step("preencher os campos de login"):
        LoginPage.fill_login(driver, "40065661826", "Valido123@")
    with allure.step("Realizaro login"):
        LoginPage.perform_login(driver)
