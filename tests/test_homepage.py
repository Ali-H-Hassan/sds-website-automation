import pytest
import datetime
from playwright.sync_api import sync_playwright
from pages.homepage import HomePage

# Setup Playwright browser context (session level)
@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

# Create a new page for each test (function level)
@pytest.fixture(scope="function")
def page(playwright_context):
    page = playwright_context.new_page()
    yield page
    page.close()

# Verify homepage title and URL
def test_homepage_title_and_url(page):
    home_page = HomePage(page)
    home_page.open_url("https://s-d-s.co.uk/")
    
    # Assert URL is correct
    current_url = page.url
    assert "https://s-d-s.co.uk/" in current_url, f"Expected URL to contain 'https://s-d-s.co.uk/', got {current_url}"
    
    # Assert title is as expected
    expected_title = "Social Housing Development Software | SDS UK"
    title = home_page.get_title()
    assert title == expected_title, f"Expected title: '{expected_title}', got '{title}'"

# Verify footer, logo, and 'Available Now' navigation
def test_homepage_footer_and_elements(page):
    home_page = HomePage(page)
    home_page.open_url("https://s-d-s.co.uk/")
    
    # Assert footer contains current year
    current_year = str(datetime.datetime.now().year)
    footer_text = home_page.get_footer_text()
    assert current_year in footer_text, f"Footer missing current year {current_year}."
    
    # Assert logo is visible
    assert home_page.is_logo_displayed(), "Logo not displayed."
    
    # Assert navigation to news page works
    home_page.click_available_now()
    new_url = page.url
    expected_news_segment = "news/sds-introduces-landval-cloud"
    assert expected_news_segment in new_url, f"Navigation failed. URL: {new_url}"
