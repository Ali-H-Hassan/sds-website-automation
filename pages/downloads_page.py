from pages.base_page import BasePage

class DownloadsPage(BasePage):
    def get_download_link(self, product_name: str) -> str:
        """
        Returns the download link (href attribute) for a download button matching the provided product name.
        
        Example product_name values: "SDS Report Designer", "SDS StockProfiler", "SDS Landval", "SDS ProVal", "SDS Sequel"
        """
        selector = f"a:has-text('{product_name}')"
        self.wait_for_selector(selector)
        return self.page.get_attribute(selector, "href")