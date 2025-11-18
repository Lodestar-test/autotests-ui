from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_word = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_word).to_be_visible()
    expect(courses_word).to_have_text('Courses')

    noresults_phrase = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(noresults_phrase).to_be_visible()
    expect(noresults_phrase).to_have_text('There is no results')

    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    results_long_phrase = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_long_phrase).to_be_visible()
    expect(results_long_phrase).to_have_text('Results from the load test pipeline will be displayed here')