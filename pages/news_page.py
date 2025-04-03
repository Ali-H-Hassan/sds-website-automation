from pages.base_page import BasePage

class NewsPage(BasePage):
    # Selectors for the news article page
    ARTICLE_TITLE = "h1.pwr-post-featured__title"  # Article title element

    # Comment form selectors (using stable attribute names)
    COMMENT_FORM = ".pwr-post-comments"
    COMMENT_FIRST_NAME = "input[name='firstname']"
    COMMENT_LAST_NAME = "input[name='lastname']"
    COMMENT_EMAIL = "input[name='email']"
    COMMENT_WEBSITE = "input[name='website']"
    COMMENT_TEXT = "textarea[name='comment']"
    COMMENT_SUBMIT = "input.hs-button.primary"

    # Navigation controls on the article page
    PREVIOUS_ARROW = "a.pwr-prev-next-nav__link[aria-label='Previous Page']"
    NEXT_ARROW = "a.pwr-prev-next-nav__link[aria-label='Next Page']"
    NEWS_LISTING_ICON = "div.pwr-prev-next-nav__container a[aria-label='Go Back']"

    # News listing page elements
    LOAD_MORE_POSTS_BUTTON = "#pwr-btn-load-more"
    
    # Filter options container and its items
    FILTER_CONTAINER = "div.pwr-filter"
    FILTER_LIST_ITEMS = "ul.pwr-filter__list li a.pwr-filter__link"
    FILTER_DROPDOWN = "div.pwr-filter__dropdown select"

    # Methods for interacting with the article page
    
    def get_article_title(self) -> str:
        """
        Returns the text of the article title.
        """
        self.wait_for_selector(self.ARTICLE_TITLE)
        return self.page.inner_text(self.ARTICLE_TITLE)

    def fill_comment_form(self, first_name: str, last_name: str, email: str, comment: str, website: str = ""):
        """
        Fills in the comment form with the provided details.
        """
        self.wait_for_selector(self.COMMENT_FORM)
        self.type_text(self.COMMENT_FIRST_NAME, first_name)
        self.type_text(self.COMMENT_LAST_NAME, last_name)
        self.type_text(self.COMMENT_EMAIL, email)
        if website:
            self.type_text(self.COMMENT_WEBSITE, website)
        self.type_text(self.COMMENT_TEXT, comment)

    def submit_comment(self):
        """
        Submits the comment form.
        """
        self.click(self.COMMENT_SUBMIT)

    def click_previous_arrow(self):
        """
        Clicks the "Previous" arrow to navigate to the previous article.
        """
        self.click(self.PREVIOUS_ARROW)

    def click_next_arrow(self):
        """
        Clicks the "Next" arrow to navigate to the next article.
        """
        self.click(self.NEXT_ARROW)

    def click_news_listing_icon(self):
        """
        Clicks the icon between the Previous and Next arrows to go back to the news listing.
        """
        self.click(self.NEWS_LISTING_ICON)

    def click_load_more_posts(self):
        """
        Clicks the "Load more posts" button to load additional news articles.
        """
        self.click(self.LOAD_MORE_POSTS_BUTTON)

    def select_filter_option(self, filter_text: str):
        """
        Selects a filter option from the filter list based on its visible text.
        """
        selector = f"{self.FILTER_CONTAINER} a:has-text('{filter_text}')"
        self.wait_for_selector(selector)
        self.click(selector)

    def select_filter_from_dropdown(self, filter_text: str):
        """
        Selects a filter option from the mobile dropdown using the visible label.
        """
        self.wait_for_selector(self.FILTER_DROPDOWN)
        self.page.select_option(self.FILTER_DROPDOWN, label=filter_text)

    def click_article_by_title(self, article_title: str):
        """
        Clicks on an article from the news listing based on the article title.
        """
        selector = f"a.pwr-post-item:has-text('{article_title}')"
        self.wait_for_selector(selector)
        self.click(selector)