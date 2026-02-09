from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-title-text', 'Title')
        self.create_exercise_button = Button(page, f'{identifier}-create-exercise-button', 'Create exercise')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')

        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()
