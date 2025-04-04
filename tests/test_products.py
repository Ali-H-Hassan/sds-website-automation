import pytest
from playwright.sync_api import sync_playwright

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

def test_landval_product_page(page):
    """
    Validate that selecting the LANDVAL product loads the correct product page with expected content.
    Steps:
      1. Open the homepage.
      2. Scroll down to the 'Browse Our Products' section.
      3. Click on the 'Read More' link for the LANDVAL product.
      4. Verify that the URL contains 'landval' and key elements are present.
    """
    # Open the homepage.
    page.goto("https://s-d-s.co.uk/")

    # Scroll down to the LANDVAL product "Read More" link.
    product_selector = "a:has-text('Read More')"
    page.eval_on_selector(product_selector, "el => el.scrollIntoView({behavior: 'smooth', block: 'center'})")

    # Click on the LANDVAL product "Read More" link.
    page.click(product_selector)

    # Verify that the URL now contains "landval".
    current_url = page.url.lower()
    assert "landval" in current_url, f"Expected URL to contain 'landval', but got {current_url}"

    # Verify key elements on the LANDVAL product page.
    book_demo = page.query_selector("a:has-text('Book a Demo Now')")
    assert book_demo is not None, "Book a Demo Now button not found on the LANDVAL product page"

    download_pdf = page.query_selector("a:has-text('Download PDF')")
    assert download_pdf is not None, "Download PDF button not found on the LANDVAL product page"

    # Verify that the new demo section is present.
    demo_section = page.query_selector("div.row-fluid-wrapper.row-depth-1.row-number-21.dnd-section.dnd_area-row-9-padding.dnd_area-row-9-force-full-width-section")
    assert demo_section is not None, "Demo section not found on the LANDVAL product page"