import pytest
from playwright.sync_api import sync_playwright
from pages.contact_forms import ContactForms

# Create a playwright browser context for tests
@pytest.fixture(autouse=True, scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

# Open a new page for each test
@pytest.fixture(scope="function")
def page(playwright_context):
    page = playwright_context.new_page()
    yield page
    page.close()

# Set up the contact form page
@pytest.fixture
def contact_form(page):
    page.goto("https://s-d-s.co.uk/")
    page.wait_for_selector(ContactForms.GET_IN_TOUCH_FORM)
    return ContactForms(page)

# Positive test: Valid form submission should have no errors
def test_valid_get_in_touch_form(contact_form, page):
    contact_form.fill_get_in_touch_form(
        first_name="John",
        last_name="Doe",
        phone="+1234567890",
        email="john.doe1@gmail.com",
        company="Acme Corp",
        message="This is a test message."
    )
    errors = page.query_selector_all(".hs-error-msg")
    assert not errors, "Unexpected error messages found on valid form input."

# Negative test: Required field validation for empty fields
@pytest.mark.parametrize("field, selector", [
    ("first_name", ContactForms.FIRST_NAME),
    ("last_name", ContactForms.LAST_NAME),
    ("phone", ContactForms.PHONE),
    ("email", ContactForms.EMAIL),
    ("company", ContactForms.COMPANY),
])
def test_required_field_validation(field, selector, contact_form, page):
    valid_data = {
        "first_name": "John",
        "last_name": "Doe",
        "phone": "+1234567890",
        "email": "john.doe1@gmail.com",
        "company": "Acme Corp",
        "message": "Test message."
    }
    valid_data[field] = ""  # Clear the field under test
    contact_form.fill_get_in_touch_form(
        first_name=valid_data["first_name"],
        last_name=valid_data["last_name"],
        phone=valid_data["phone"],
        email=valid_data["email"],
        company=valid_data["company"],
        message=valid_data["message"]
    )
    contact_form.submit_get_in_touch_form()
    page.wait_for_selector(".hs-error-msg")
    error_text = page.text_content(".hs-error-msg")
    assert "Please complete this required field." in error_text, f"Expected required field error for {field}"

# Negative test: Invalid phone number
def test_invalid_phone_number(contact_form, page):
    contact_form.fill_get_in_touch_form(
        first_name="John",
        last_name="Doe",
        phone="invalid_phone",
        email="john.doe1@gmail.com",
        company="Acme Corp",
        message="Test message."
    )
    contact_form.submit_get_in_touch_form()
    page.wait_for_selector(".hs-error-msg")
    error_text = page.text_content(".hs-error-msg")
    assert "A valid phone number may only contain numbers, +()-. or x" in error_text, "Expected invalid phone number error"

# Negative test: Invalid email address
def test_invalid_email(contact_form, page):
    contact_form.fill_get_in_touch_form(
        first_name="John",
        last_name="Doe",
        phone="+1234567890",
        email="invalid_email",
        company="Acme Corp",
        message="Test message."
    )
    contact_form.submit_get_in_touch_form()
    page.wait_for_selector(".hs-error-msg")
    error_text = page.text_content(".hs-error-msg")
    assert "Email must be formatted correctly." in error_text, "Expected invalid email error"
