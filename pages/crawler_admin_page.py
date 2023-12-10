from assertpy import assert_that
from seleniumbase import BaseCase


class CrawlerAdminPage(BaseCase):
    CRAWLER_HEADING_ELEMENT = "//h1[normalize-space()='WP Crawler admn panel']"
    CRAWL_BUTTON = "//button[@id='wpcrawler-crawl-button']"
    CRAWLER_ADMIN_PANEL_TAB = "//a[.='WP Crawler admn panel']"
    CRAWL_LINKS = "//li[contains(.,'http://test.local')]"
    TOOLS_TAB = "//div[normalize-space()='Tools']"
    CRAWL_FIRST_LINK = "//li[.='http://test.local']"
    CRAWLER_SCHEDULE_TIME = "//p[@id='wpcrawler-cron-crawl-status']"

    def verify_crawler_page_loads(self):
        assert_that(self.is_element_present(self.CRAWLER_HEADING_ELEMENT)).is_true()
        assert_that(self.is_element_present(self.CRAWL_BUTTON)).is_true()

    def click_on_tools_tab(self):
        self.click(self.TOOLS_TAB)

    def click_crawler_admin_tab(self):
        self.click(self.CRAWLER_ADMIN_PANEL_TAB)

    def goto_crawler_admin_page(self):
        self.click_on_tools_tab()
        self.click_crawler_admin_tab()
        self.verify_crawler_page_loads()

    def trigger_crawl(self):
        self.click(self.CRAWL_BUTTON)

    def get_crawler_results(self):
        # Get all li elements on the page
        li_elements = self.find_elements("li")
        return len(li_elements)