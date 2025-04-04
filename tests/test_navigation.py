import pytest
from playwright.sync_api import sync_playwright
from pages.homepage import HomePage

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(playwright_context):
    page = playwright_context.new_page()
    yield page
    page.close()

@pytest.mark.parametrize("nav_item, expected_url_fragment, expected_title", [
    ("Products", "products", "Products"),
    ("Consultancy", "consultancy", "Consultancy"),
    ("SDS Services", "services", "SDS Services"),
    ("Support", "support", "Support"),
    ("Events", "events", "Events"),
    ("Latest News", "blog", "SDS Blog"),
    ("Contact", "contact", "Contact")
])
def test_navigation_menu(page, nav_item, expected_url_fragment, expected_title):
    """
    Validate that clicking on a navigation menu item redirects to a URL containing the expected fragment
    and that the page title matches the expected title.
    """
    home_page = HomePage(page)
    home_page.open_url("https://s-d-s.co.uk/")
    
    # Click the navigation menu item based on its visible text.
    home_page.click_navigation_item_by_text(nav_item)
    
    # Verify the URL contains the expected fragment.
    current_url = page.url.lower()
    assert expected_url_fragment in current_url, (
        f"Navigation for '{nav_item}' did not navigate to a URL containing '{expected_url_fragment}'. "
        f"Current URL: {current_url}"
    )
    
    # Verify the page title matches the expected title.
    title = home_page.get_title()
    assert title == expected_title, (
        f"Expected title '{expected_title}' for '{nav_item}', but got '{title}'."
    )