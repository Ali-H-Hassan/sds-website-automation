from pages.base_page import BasePage

class ProductsPage(BasePage):
    # Selector for product item on the /products page (example for Landval Cloud)
    PRODUCT_ITEM = ".pwr-image-box__back.pwr-3D-box__info-box a.pwr-image-box__more-link"
    
    # Selectors for individual product page actions
    BOOK_A_DEMO_BUTTON = ".pwr-sec-cta__cta--vertical.pwr-cta--custom-03 a.pwr-cta_button"
    DOWNLOAD_PDF_BUTTON = ".pwr-sec-cta__cta--vertical.pwr-cta--custom-01 a.pwr-cta_button"
    
    # Selectors for the "Wish to Know More?" form (specific to LANDVAL product page)
    WISH_TO_KNOW_MORE_TITLE = "#wish-to-know-more"

    WISH_FORM_FIRST_NAME = "input#firstname-25c7bb2a-eae6-4dd1-b936-e990b011cef5_13"
    WISH_FORM_LAST_NAME = "input#lastname-25c7bb2a-eae6-4dd1-b936-e990b011cef5_13"
    WISH_FORM_EMAIL = "input#email-25c7bb2a-eae6-4dd1-b936-e990b011cef5_13"
    WISH_FORM_SUBMIT = "input.hs-button.primary.large"

    # ---------------------------
    # Methods for Products Listing Page
    # ---------------------------
    def get_product_link(self) -> str:
        """
        Returns the href attribute of the product item link on the products listing page.
        This can be used to verify if it incorrectly redirects to Google.
        """
        self.wait_for_selector(self.PRODUCT_ITEM)
        return self.page.get_attribute(self.PRODUCT_ITEM, "href")

    # ---------------------------
    # Methods for Individual Product Page
    # ---------------------------
    def click_book_a_demo(self):
        """
        Clicks the 'Book a Demo Now' button on the individual product page.
        """
        self.wait_for_selector(self.BOOK_A_DEMO_BUTTON)
        self.click(self.BOOK_A_DEMO_BUTTON)

    def click_download_pdf(self):
        """
        Clicks the 'Download PDF' button on the individual product page.
        """
        self.wait_for_selector(self.DOWNLOAD_PDF_BUTTON)
        self.click(self.DOWNLOAD_PDF_BUTTON)

    def is_wish_to_know_more_form_displayed(self) -> bool:
        """
        Verifies that the 'Wish to Know More?' form is displayed by checking the presence of the title.
        """
        try:
            self.wait_for_selector(self.WISH_TO_KNOW_MORE_TITLE)
            return True
        except Exception:
            return False

    def fill_wish_to_know_more_form(self, first_name: str, last_name: str, email: str):
        """
        Fills the 'Wish to Know More?' form fields with the provided data.
        """
        self.wait_for_selector(self.WISH_FORM_FIRST_NAME)
        self.type_text(self.WISH_FORM_FIRST_NAME, first_name)
        self.type_text(self.WISH_FORM_LAST_NAME, last_name)
        self.type_text(self.WISH_FORM_EMAIL, email)

    def submit_wish_to_know_more_form(self):
        """
        Submits the 'Wish to Know More?' form.
        """
        self.wait_for_selector(self.WISH_FORM_SUBMIT)
        self.click(self.WISH_FORM_SUBMIT)