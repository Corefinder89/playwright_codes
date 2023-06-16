from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.demoblaze.com/index.html")
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").click()
    page.locator("#loginusername").fill("test")
    page.locator("#loginpassword").click()
    page.locator("#loginpassword").fill("test")
    page.get_by_role("button", name="Log in").click()
    page.get_by_role("link", name="Phones").click()
