from components.base_component import BaseComponent
from playwright.sync_api import expect


class CreateCourseExerciseFormComponent(BaseComponent):
    def click_delete_button(self, index: int):
        # локатор инициализируется непосредственно в методе!
        delete_button = self.page.get_by_test_id(
            f'create-course-exercise-{index}-box-toolbar-delete-exercise-button'
        )
        delete_button.click()

    # переименовали check_visible_create_exercise_form в check_visible
    def check_visible(self, index: int, title: str, description: str):
        # переименовали exercise_subtitle в subtitle
        subtitle = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-subtitle-text")
        # переименовали exercise_title_input в title_input
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        # переименовали exercise_description_input в description_input
        description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input")

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        # переименовали exercise_title_input в title_input
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        # переименовали exercise_description_input в description_input
        description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input")

        title_input.fill(title)
        expect(title_input).to_have_value(title)

        description_input.fill(description)
        expect(description_input).to_have_value(description)
