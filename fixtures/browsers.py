import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest  # Импортируем класс SubRequest для аннотации
import allure


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # Создаем контекст для новой сессии браузера
    context.tracing.start(screenshots=True, snapshots=True, sources=True)   # Включаем трейсинг

    yield context.new_page()    # Открываем новую страницу в контексте
    # yield browser.new_page()

    # В данном случае request.node.name содержит название текущего автотеста
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл)
    browser.close() # Закрываем браузер

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')

# @pytest.fixture
# def chromium_page() -> Page:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         yield browser.new_page()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.vizit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()


    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture(scope='function')
# добавили request: SubRequest, чтобы подставлялось имя теста из метаданных
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг

    yield context.new_page()

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл)
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
