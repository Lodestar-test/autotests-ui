from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
        # wait_until='networkidle'  # чтобы починить третью ошибку на выполнение js скрипта
    )

    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = 'New Text'
        """
    )