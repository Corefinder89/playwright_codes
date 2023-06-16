from playwright.sync_api import Page
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"storage_state": "auth.json"}


def test_example(page: Page) -> None:
    page.goto("https://www.demoblaze.com/index.html")
    page.locator("div:nth-child(2) > .card > a").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()
    page.get_by_role("button", name="Place Order").click()
    page.get_by_label("Total: 820").click()
    page.get_by_label("Total: 820").fill("Test")
    page.get_by_label("Total: 820").press("Tab")
    page.get_by_label("Country:").fill("test")
    page.get_by_label("Country:").press("Tab")
    page.get_by_label("City:").fill("test")
    page.get_by_label("City:").press("Tab")
    page.get_by_label("Credit card:").fill("test")
    page.get_by_label("Credit card:").press("Tab")
    page.get_by_label("Month:").fill("test")
    page.get_by_label("Month:").press("Tab")
    page.get_by_label("Year:").fill("test")
    page.get_by_role("button", name="Purchase").click()
    page.get_by_role("button", name="OK").click()
