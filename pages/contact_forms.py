from pages.base_page import BasePage

class ContactForms(BasePage):
    # Selector for the Get in Touch form (using its unique form id)
    GET_IN_TOUCH_FORM = "form#hsForm_3ff8d7d3-ea77-4fb1-9a68-500ca40acec7_9459"
    
    # Individual field selectors (using their unique ids)
    FIRST_NAME = "#firstname-3ff8d7d3-ea77-4fb1-9a68-500ca40acec7_9459"
    LAST_NAME = "#lastname-3ff8d7d3-ea77-4fb1-9a68-500ca40acec7_9459"
    PHONE = "#phone-3ff8d7d3-ea77-4fb1-9a68-500ca40acec7_9459"
    EMAIL = "#email-3ff8d7d3-ea77-4fb1-9a68-500ca40acec7_9459"
    COMPANY = "#company-3ff8d7d3-ea77-4fb1-9a68-500ca40acec7_9459"
    MESSAGE = "#message-3ff8d7d3-ea77-4fb1-9a68-500ca40acec7_9459"
    
    # Submit button for the form
    SUBMIT_BUTTON = "form#hsForm_3ff8d7d3-ea77-4fb1-9a68-500ca40acec7_9459 input[type='submit']"
    
    # For the Enquiry Type checkboxes, we'll target them by name and value.
    # (e.g., input[name="enquiry_type"][value="I'm interested in SDS software"])
    
    def fill_get_in_touch_form(self, first_name: str, last_name: str, phone: str, email: str, company: str, message: str):
        """
        Fills the 'Get in Touch' form with the provided data.
        """
        self.wait_for_selector(self.GET_IN_TOUCH_FORM)
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.PHONE, phone)
        self.type_text(self.EMAIL, email)
        self.type_text(self.COMPANY, company)
        self.type_text(self.MESSAGE, message)
    
    def select_enquiry_type(self, value: str):
        """
        Selects an enquiry type checkbox based on its value.
        
        Example value: "I'm interested in SDS software"
        """
        selector = f"input[name='enquiry_type'][value=\"{value}\"]"
        self.wait_for_selector(selector)
        self.click(selector)
    
    def submit_get_in_touch_form(self):
        """
        Submits the 'Get in Touch' form.
        """
        self.wait_for_selector(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)