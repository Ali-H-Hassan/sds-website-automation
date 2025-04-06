import pytest
from playwright.sync_api import sync_playwright

VIEWPORTS = [
    {"name": "Desktop", "width": 1280, "height": 800, "is_mobile": False},
    {"name": "Tablet",  "width": 768,  "height": 1024, "is_mobile": True},
    {"name": "Mobile",  "width": 375,  "height": 667,  "is_mobile": True}
]

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        yield browser
        browser.close()

@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_responsive_design(browser, viewport):
    # Create a new browser context with the specified viewport
    context = browser.new_context(
        viewport={"width": viewport["width"], "height": viewport["height"]},
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    )
    page = context.new_page()
    page.goto("https://s-d-s.co.uk/")
    
    # Accept the cookie popup if it appears
    cookie_accept_selector = "#hs-eu-confirmation-button"
    try:
        page.wait_for_selector(cookie_accept_selector, timeout=3000)
        page.click(cookie_accept_selector)
        print("Cookie accepted, waiting 1 second...")
        page.wait_for_timeout(1000)  # Wait 1 second (1000 ms)
    except Exception:
        # Cookie popup did not appear, continue with the test.
        pass

    # Check that the SDS logo is visible (confirming the page loaded correctly)
    logo_selector = "img[alt='SDS-logo-white']"
    logo = page.wait_for_selector(logo_selector, timeout=5000)
    assert logo.is_visible(), f"SDS logo not visible on {viewport['name']} view"
    
    # Verify navigation behavior:
    # For mobile view, the hamburger menu (using the corrected selector) should be visible.
    # For desktop view, it should not be visible.
    hamburger = page.query_selector("#pwr-js-burger__trigger-open")
    if viewport["is_mobile"]:
        assert hamburger is not None, f"Hamburger menu button not found on {viewport['name']} view"
        assert hamburger.is_visible(), f"Hamburger menu button not visible on {viewport['name']} view"
    else:
        if hamburger:
            assert not hamburger.is_visible(), f"Hamburger menu button should not be visible on {viewport['name']} view"
    
    # Verify the page title is as expected
    expected_title = "Social Housing Development Software | SDS UK"
    actual_title = page.title()
    assert actual_title == expected_title, f"Expected title '{expected_title}' on {viewport['name']} view, but got '{actual_title}'"
    
    context.close()
