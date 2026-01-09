from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.email = page.get_by_test_id(f'{identifier}-email-input').locator('input')
        self.password = page.get_by_test_id(f'{identifier}-password-input').locator('input')

    def fill(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)

    def check_visible(self, email: str | None = None, password: str | None = None):
        expect(self.email).to_be_visible()
        expect(self.password).to_be_visible()

        if email is not None:
            if email:
                expect(self.email).to_have_value(email)
            else:
                expect(self.email).to_be_empty()

        if password is not None:
            if password:
                expect(self.password).to_have_value(password)
            else:
                expect(self.password).to_be_empty()
