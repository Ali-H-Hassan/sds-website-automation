from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators for homepage elements
    LOGO = ".pwr-header-logo .pwr-header__logo-link"
    NAVIGATION_MENU = "div[aria-label='main']"
    AVAILABLE_NOW_BUTTON = ".pwr-sec-cta__cta-wrapper a.pwr-cta_button"
    FOOTER = ".pwr-footer"

    def is_logo_displayed(self) -> bool:
        """
        Verify that the homepage logo is visible.
        """
        try:
            self.wait_for_selector(self.LOGO)
            return True
        except Exception as e:
            return False

    def click_logo(self):
        """
        Click the homepage logo to navigate back to the homepage.
        """
        self.click(self.LOGO)

    def click_available_now(self):
        """
        Click the 'Available Now' button to navigate to the specified news article.
        """
        self.click(self.AVAILABLE_NOW_BUTTON)

    def click_navigation_item_by_text(self, item_text: str):
        """
        Click on a navigation menu item based on its visible text.
        
        :param item_text: The text of the navigation item (e.g., 'Products', 'Consultancy').
        """
        # Construct a selector to find the anchor tag within the navigation menu that contains the specified text.
        selector = f"div[aria-label='main'] a:has-text('{item_text}')"
        self.wait_for_selector(selector)
        self.click(selector)

    def get_footer_text(self) -> str:
        """
        Retrieve the text content of the footer.
        """
        self.wait_for_selector(self.FOOTER)
        return self.page.inner_text(self.FOOTER)