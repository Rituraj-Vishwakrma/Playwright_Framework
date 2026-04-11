import pytest
# Import pytest to use fixtures and hooks

from playwright.sync_api import sync_playwright
# Import Playwright sync API


# 🔹 HOOK: Runs once BEFORE all tests start
def pytest_sessionstart(session):
    print("=== Test Execution Started ===")
    # This runs before any test is executed


# 🔹 HOOK: Runs once AFTER all tests finish
def pytest_sessionfinish(session):
    print("=== Test Execution Finished ===")
    # This runs after all tests are completed


# 🔹 FIXTURE: Provides browser page to tests
@pytest.fixture
def page():

    # Start Playwright
    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(headless=False)

        # Open new tab
        page = browser.new_page()

        # Give page to test
        yield page

        # Cleanup after test
        browser.close()

        #hooks for global lifecycle control and fixtures for reusable test setup.