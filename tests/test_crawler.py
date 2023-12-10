import pytest
from assertpy import assert_that

from pages.crawler_admin_page import CrawlerAdminPage
from pages.wp_login_page import WpLoginPage
from tests.base_test import BaseTest


class CrawlerTest(BaseTest, CrawlerAdminPage, WpLoginPage):

    @pytest.mark.crawler
    def test_verify_crawler_admin_page(self):
        self.goto_crawler_admin_page()
        self.verify_crawler_page_loads()

    @pytest.mark.crawler
    def test_trigger_manual_crawl(self):
        self.goto_crawler_admin_page()
        self.verify_crawler_page_loads()
        self.trigger_crawl()
        self.refresh()
        self.sleep(5)
        assert_that(self.is_element_present(self.CRAWLER_SCHEDULE_TIME)).is_true()
        assert_that(self.is_element_present(self.CRAWL_FIRST_LINK)).is_true()



