from pages.base_page import BasePage

class OpenElearningPage(BasePage):
    BOOK_TRAINING_BUTTON = "a:has-text('Book Training')"
    COURSE_INFORMATION_BUTTON = "a:has-text('Course Information')"

    def is_book_training_displayed(self) -> bool:
        """
        Verifies that the 'Book Training' button is displayed.
        """
        try:
            self.wait_for_selector(self.BOOK_TRAINING_BUTTON)
            return True
        except Exception:
            return False

    def click_book_training(self):
        """
        Clicks the 'Book Training' button. This button is expected to do nothing.
        """
        self.wait_for_selector(self.BOOK_TRAINING_BUTTON)
        self.click(self.BOOK_TRAINING_BUTTON)

    def click_course_information(self) -> str:
        """
        Clicks the 'Course Information' button and returns the href attribute for verification.
        """
        self.wait_for_selector(self.COURSE_INFORMATION_BUTTON)
        course_info_link = self.page.get_attribute(self.COURSE_INFORMATION_BUTTON, "href")
        self.click(self.COURSE_INFORMATION_BUTTON)
        return course_info_link