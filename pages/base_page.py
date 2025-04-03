import logging
import os
from playwright.sync_api import Page, TimeoutError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasePage:
    DEFAULT_TIMEOUT = 30000  

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        try:
            logger.info(f"Navigating to URL: {url}")
            self.page.goto(url, timeout=self.DEFAULT_TIMEOUT)
        except Exception as e:
            logger.error(f"Error navigating to {url}: {e}")
            self.take_screenshot("open_url_error")
            raise

    def get_title(self) -> str:
        try:
            title = self.page.title()
            logger.info(f"Retrieved page title: {title}")
            return title
        except Exception as e:
            logger.error(f"Error retrieving title: {e}")
            self.take_screenshot("get_title_error")
            raise

    def wait_for_selector(self, selector: str, timeout: int = DEFAULT_TIMEOUT):
        try:
            logger.info(f"Waiting for selector: {selector}")
            self.page.wait_for_selector(selector, timeout=timeout)
        except TimeoutError as e:
            logger.error(f"Timeout waiting for selector {selector}: {e}")
            self.take_screenshot("wait_for_selector_timeout")
            raise
        except Exception as e:
            logger.error(f"Error waiting for selector {selector}: {e}")
            self.take_screenshot("wait_for_selector_error")
            raise

    def click(self, selector: str):
        try:
            logger.info(f"Clicking on element: {selector}")
            self.page.click(selector, timeout=self.DEFAULT_TIMEOUT)
        except Exception as e:
            logger.error(f"Error clicking on {selector}: {e}")
            self.take_screenshot("click_error")
            raise

    def type_text(self, selector: str, text: str):
        try:
            logger.info(f"Typing text into element: {selector}")
            self.page.fill(selector, text)
        except Exception as e:
            logger.error(f"Error typing text into {selector}: {e}")
            self.take_screenshot("type_text_error")
            raise

    def take_screenshot(self, name: str):
        try:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
            self.page.screenshot(path=screenshot_path)
            logger.info(f"Screenshot taken: {screenshot_path}")
        except Exception as e:
            logger.error(f"Error taking screenshot {name}: {e}")