import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        yield browser
        browser.close()

def test_accessibility_homepage(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://s-d-s.co.uk/")
    
    # Accept the cookie popup if it appears
    cookie_accept_selector = "#hs-eu-confirmation-button"
    try:
        page.wait_for_selector(cookie_accept_selector, timeout=3000)
        page.click(cookie_accept_selector)
    except Exception:
        pass

    # Inject the axe-core script from a CDN into the page
    axe_script_url = "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.6.2/axe.min.js"
    page.add_script_tag(url=axe_script_url)
    
    # Run axe accessibility analysis on the current page
    result = page.evaluate("async () => { return await axe.run(); }")
    
    # Extract violations from the result
    violations = result.get("violations", [])
    
    # Optionally, print the violations to the console for review
    if violations:
        for violation in violations:
            print(f"Axe Violation: {violation['id']} - {violation['description']}")
    
    # Assert that there are no accessibility violations
    assert len(violations) == 0, f"Accessibility violations found: {violations}"
    
    context.close()
