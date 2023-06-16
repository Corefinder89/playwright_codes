from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("hello")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_test_id("todo-title").click()
    page.get_by_role("link", name="Active").click()

    # ---------------------
    context.close()
    browser.close()
