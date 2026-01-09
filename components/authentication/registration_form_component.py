from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.email = page.get_by_test_id(f'{identifier}-email-input').locator('input')
        self.username = page.get_by_test_id(f'{identifier}-username-input').locator('input')
        self.password = page.get_by_test_id(f'{identifier}-password-input').locator('input')

    def fill(self, email: str, username: str, password: str):
        self.email.fill(email)
        self.username.fill(username)
        self.password.fill(password)

    def check_visible(self, email: str | None = None, username: str | None = None, password: str | None = None):
        expect(self.email).to_be_visible()
        expect(self.password).to_be_visible()

        if email is not None:
            if email:
                expect(self.email).to_have_value(email)
            else:
                expect(self.email).to_be_empty()

        if username is not None:
            if username:
                expect(self.username).to_have_value(username)
            else:
                expect(self.username).to_be_empty()

        if password is not None:
            if password:
                expect(self.password).to_have_value(password)
            else:
                expect(self.password).to_be_empty()
