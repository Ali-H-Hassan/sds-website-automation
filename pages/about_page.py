from pages.base_page import BasePage

class AboutPage(BasePage):
    # Selectors for About page elements
    OUR_SOFTWARE_BUTTON = "a:has-text('Our Software')"
    SUPPORT_PORTAL_BUTTON = "a:has-text('Login to our Support Portal')"

    def click_our_software(self):
        """
        Clicks the 'Our Software' button, which should redirect the user to the Products page.
        """
        self.wait_for_selector(self.OUR_SOFTWARE_BUTTON)
        self.click(self.OUR_SOFTWARE_BUTTON)

    def click_support_portal(self):
        """
        Clicks the 'Login to our Support Portal' button.
        Since it opens in a new tab, this method returns the target URL for validation.
        """
        self.wait_for_selector(self.SUPPORT_PORTAL_BUTTON)
        # Optionally, get the href attribute to verify it matches the expected external URL.
        support_portal_url = self.page.get_attribute(self.SUPPORT_PORTAL_BUTTON, "href")
        self.click(self.SUPPORT_PORTAL_BUTTON)
        return support_portal_url