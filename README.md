# SDS Website Automation Tests

This repository contains automated tests for the SDS website (www.s-d-s.co.uk) using **Playwright** and **Pytest**.

## Requirements

- Python 3.7+
- Pytest 7.2.2
- Playwright 1.30.0

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sds-website-automation.git
cd sds-website-automation
```

### 2. Create & Activate a Virtual Environment (Recommended)

**For Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install pytest==7.2.2 playwright==1.30.0
playwright install
```

## Running Tests

### Run All Tests

```bash
python run_tests.py
```

### Run a Specific Test File

```bash
pytest tests/test_name.py
```

## Test Coverage

This test suite covers the following requirements from the assessment:

1. **Homepage Verification**: Tests verify title and URL are correct
2. **Navigation Test**: Validates all main navigation sections load correctly with appropriate URLs and titles
3. **Product Information Test**: Checks product pages content including "Book a Demo Now" and "Download PDF" buttons
4. **Contact Form Test**: Tests form validation including required fields, invalid phone numbers, and invalid emails
5. **Responsive Design Test**: Tests website behavior across multiple viewport sizes (Desktop, Tablet, Mobile)
6. **Accessibility Testing**: Validates website accessibility using Lighthouse

## Implementation Details

### Key Features

- **Page Object Model**: Tests use a structured POM design pattern for better maintainability
- **Responsive Testing**: Tests run on multiple viewport sizes: Desktop (1280x800), Tablet (768x1024), and Mobile (375x667)
- **Error Handling**: Comprehensive error handling with screenshots on failures
- **Logging**: Detailed logging for debugging and traceability
- **Cookie Handling**: Automatic handling of cookie consent popups
- **Parameterized Tests**: Using pytest's parametrization for efficient test coverage

### Browser Configuration

- Tests run with Chromium browser
- Tests include options for both headless and headed mode
- Browser context includes appropriate user agent configuration

### Test Isolation

- Each test uses fresh browser contexts and pages
- Test fixtures are properly scoped (session vs function level)
- No actual form submissions are made to avoid generating spam

## Test Details

### 1. Homepage Tests
- Verify correct page title and URL
- Confirm logo is displayed
- Validate footer content including current year
- Test "Available Now" button navigation

### 2. Navigation Tests
- Parameterized tests for all main navigation items:
  - Products
  - Consultancy
  - SDS Services
  - Support
  - Events
  - Latest News
  - Contact
- Verify each page loads with correct URL and title

### 3. Form Tests
- Validate required fields
- Test error messages for invalid inputs
- Verify successful form input validation

### 4. Products Tests
- Verify product page navigation
- Validate presence of key elements like "Book a Demo" button
- Confirm product-specific content appears correctly

### 5. Responsive Tests
- Test website behavior at different viewport sizes
- Validate hamburger menu appears only on mobile/tablet views
- Ensure core elements remain functional across all devices

### 6. Accessibility Tests
- Integration with Lighthouse for accessibility scoring
- Validate accessibility score meets threshold requirements
- Generate accessibility reports for compliance review

---
