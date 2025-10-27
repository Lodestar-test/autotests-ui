from playwright.sync_api import sync_playwright, expect, Request, Response

def log_request(request: Request):
    print(f'Request: {request.url}')

def log_response(response: Response):
    print(f'Response: {response.url}, {response.status}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.on('request', log_request)
    #  page.remove_listener('request', log_request)
    page.on('response', log_response)


    # def log_response_body(response):     # дополнительная информация о содержимом ответа
    #     if response.ok:
    #         print(f"Response body: {response.body()}")  # Тело ответа
    #
    #
    # page.on("response", log_response_body)

    page.wait_for_timeout(5000)
