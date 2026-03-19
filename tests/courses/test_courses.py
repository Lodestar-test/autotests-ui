import pytest
import allure

from config import settings
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.vizit(AppRoute.COURSES)
        courses_list_page.navbar.check_visible(settings.test_user.username)  # проверяем отображение компонента Navbar
        courses_list_page.sidebar.check_visible()  # проверяем отображение компонента Sidebar
        # проверяем отображение заголовка "Courses" и отображение кнопки создания курса (тулбар списка курсов):
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()  # проверяем отображение пустого блока

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.vizit(AppRoute.COURSES_CREATE)
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(file=settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10'
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.vizit(AppRoute.COURSES_CREATE)
        create_course_page.create_course_form.fill(
            title='Test data1',
            estimated_time='2 weeks',
            description='Test description1',
            max_score='100',
            min_score='10'
        )
        create_course_page.image_upload_widget.upload_preview_image(file=settings.test_data.image_png_file)
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # проверка отображения карточки курса c заданными данными на странице списка курсов
        courses_list_page.course_view.check_visible(
            index=0,
            title='Test data1',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10'
        )

        courses_list_page.course_view_menu.click_edit(index=0)
        create_course_page.create_course_form.fill(
            title='Test data2',
            estimated_time='1 month',
            description='Test description2',
            max_score='20',
            min_score='5'
        )

        # проверка изменений всех отредактированных полей
        create_course_page.create_course_form.check_visible(
            title='Test data2',
            estimated_time='1 month',
            description='Test description2',
            max_score='20',
            min_score='5'
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # проверка отображения карточки курса с обновленными данными на странице списка курсов
        courses_list_page.course_view.check_visible(
            index=0,
            title='Test data2',
            estimated_time='1 month',
            max_score='20',
            min_score='5'
        )

