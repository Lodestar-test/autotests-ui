from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
        wait_until='networkidle'
    )

    new_text = 'New Text'

    # Выполняем JS-код для замены текста заголовка
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text
        }
        """,
        new_text   # Передаём переменную из Python
    )

    page.wait_for_timeout(5000)