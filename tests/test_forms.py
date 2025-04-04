import pytest
from playwright.sync_api import sync_playwright
from pages.contact_forms import ContactForms

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

@pytest.fixture
def contact_form(page):
    # Navigate to the homepage where the "Get in Touch" form is located.
    page.goto("https://s-d-s.co.uk/")
    # Use the updated form selector from the page object.
    contact_form_selector = ContactForms.GET_IN_TOUCH_FORM
    page.wait_for_selector(contact_form_selector)
    return ContactForms(page)

def test_valid_get_in_touch_form(contact_form, page):
    """
    Positive (happy-path) test:
    Fill in the form with valid data and verify that no error messages are displayed.
    """
    contact_form.fill_get_in_touch_form(
        first_name="John",
        last_name="Doe",
        phone="+1234567890",
        email="john.doe1@gmail.com",
        company="Acme Corp",
        message="This is a test message."
    )
    # Skip selecting an enquiry option since it's not required.
    # Do not submit the form. Verify that no error messages appear.
    errors = page.query_selector_all(".hs-error-msg")
    assert not errors, "Unexpected error messages found on valid form input."

@pytest.mark.parametrize("field, selector", [
    ("first_name", ContactForms.FIRST_NAME),
    ("last_name", ContactForms.LAST_NAME),
    ("phone", ContactForms.PHONE),
    ("email", ContactForms.EMAIL),
    ("company", ContactForms.COMPANY),
])
def test_required_field_validation(field, selector, contact_form, page):
    """
    Negative test:
    Verify that leaving a required field empty shows the required field error.
    """
    valid_data = {
        "first_name": "John",
        "last_name": "Doe",
        "phone": "+1234567890",
        "email": "john.doe1@gmail.com",
        "company": "Acme Corp",
        "message": "Test message."
    }
    # Leave the specified field empty.
    valid_data[field] = ""
    contact_form.fill_get_in_touch_form(
        first_name=valid_data["first_name"],
        last_name=valid_data["last_name"],
        phone=valid_data["phone"],
        email=valid_data["email"],
        company=valid_data["company"],
        message=valid_data["message"]
    )
    # Skip selecting an enquiry option.
    contact_form.submit_get_in_touch_form()
    page.wait_for_selector(".hs-error-msg")
    error_text = page.text_content(".hs-error-msg")
    assert "Please complete this required field." in error_text, f"Expected required field error for {field}"

def test_invalid_phone_number(contact_form, page):
    """
    Negative test:
    Fill in an invalid phone number and verify the phone validation error.
    """
    contact_form.fill_get_in_touch_form(
        first_name="John",
        last_name="Doe",
        phone="invalid_phone",
        email="john.doe1@gmail.com",
        company="Acme Corp",
        message="Test message."
    )
    # Skip selecting an enquiry option.
    contact_form.submit_get_in_touch_form()
    page.wait_for_selector(".hs-error-msg")
    error_text = page.text_content(".hs-error-msg")
    assert "A valid phone number may only contain numbers, +()-. or x" in error_text, "Expected invalid phone number error"

def test_invalid_email(contact_form, page):
    """
    Negative test:
    Fill in an invalid email address and verify the email validation error.
    """
    contact_form.fill_get_in_touch_form(
        first_name="John",
        last_name="Doe",
        phone="+1234567890",
        email="invalid_email",
        company="Acme Corp",
        message="Test message."
    )
    # Skip selecting an enquiry option.
    contact_form.submit_get_in_touch_form()
    page.wait_for_selector(".hs-error-msg")
    error_text = page.text_content(".hs-error-msg")
    assert "Email must be formatted correctly." in error_text, "Expected invalid email error"
