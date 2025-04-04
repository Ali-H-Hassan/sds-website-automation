import pytest
import datetime
from playwright.sync_api import sync_playwright
from pages.homepage import HomePage

# Pytest fixture to launch Playwright browser and create a context
@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

# Fixture to create and close a new page for each test function
@pytest.fixture(scope="function")
def page(playwright_context):
    page = playwright_context.new_page()
    yield page
    page.close()

def test_homepage_title_and_url(page):
    """
    Validate that the homepage loads correctly with the expected title and URL.
    """
    home_page = HomePage(page)
    home_page.open_url("https://s-d-s.co.uk/")
    
    # Validate current URL contains the homepage base URL
    current_url = page.url
    assert "https://s-d-s.co.uk/" in current_url, f"Expected URL to contain 'https://s-d-s.co.uk/', but got {current_url}"
    
    # Update the expected title to match the actual <title>
    expected_title = "Social Housing Development Software | SDS UK"
    title = home_page.get_title()
    assert title == expected_title, f"Expected title: '{expected_title}', but got '{title}'"

def test_homepage_footer_and_elements(page):
    """
    Validate that key homepage elements are displayed and function as expected:
      - Footer displays the current year dynamically.
      - Homepage logo is visible.
      - Clicking the 'Available Now' button navigates to the correct news article.
    """
    home_page = HomePage(page)
    home_page.open_url("https://s-d-s.co.uk/")
    
    # Dynamically get the current year as a string
    current_year = str(datetime.datetime.now().year)
    
    # Validate that the footer text contains the current year
    footer_text = home_page.get_footer_text()
    assert current_year in footer_text, f"Footer does not display the current year {current_year}. Footer text: {footer_text}"
    
    # Validate that the homepage logo is displayed
    assert home_page.is_logo_displayed(), "Homepage logo is not displayed"
    
    # Click the "Available Now" button and verify redirection to the news article page
    home_page.click_available_now()
    new_url = page.url
    expected_news_segment = "news/sds-introduces-landval-cloud"
    assert expected_news_segment in new_url, (
        f"Clicking 'Available Now' did not navigate to the expected page. URL: {new_url}"
    )