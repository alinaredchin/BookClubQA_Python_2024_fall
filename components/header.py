from playwright.sync_api import Page, expect
from core.settings import base_url
import allure


class Header:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем Хэдер на главной странице")
    def visit(self):
        self.page.goto(base_url)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_on_login_button(self):
        self.page.locator('(//a[@class="btn btn-outline-light mb-2 me-2 ms-3"])[1]').click()

    @allure.step("Кликаем на кнопку 'Регистрация'")
    def click_on_registration_button(self):
        self.page.get_by_test_id("signup").click()

    @allure.step("Проверяем видимость кнопки 'Создать объявление'")
    def create_listing_button_should_be_visible(self):
        expect(self.page.get_by_test_id("create-listing")).to_be_visible()

    @allure.step("Кликаем на кнопку 'Найти репетитора'")
    def click_on_find_tutor_button(self):
        self.page.locator("//li/a[@href = '/list/']").click()

    @allure.step("Проверяем видимость кнопки 'Поддержка'")
    def support_button_should_be_visible(self):
        button = self.page.locator("//a[contains(@class, 'btn') and text()='Поддержка']")
        expect(button).to_be_visible()

    @allure.step("Кликаем на кнопку 'Поддержка'")
    def click_on_support_button(self):
        button = self.page.locator("//a[contains(@class, 'btn') and text()='Поддержка']")
        button.click()
        expect(self.page).to_have_url("https://t.me/misleplav_support_bot")

    @allure.step("Проверяем видимость кнопки 'Войти'")
    def login_button_should_be_visible(self):
        button = self.page.locator('(//a[@class="btn btn-outline-light mb-2 me-2 ms-3"])[1]')
        assert button.is_visible()<<<<<<< TC_00.002.002.001
        
    @allure.step("Проверяем видимость кнопки 'Стать репетитором'")
    def become_a_tutor_button_should_be_visible(self):
        button = self.page.locator('//a[@class="btn btn-light rounded d-none d-sm-inline btn-lg"]')