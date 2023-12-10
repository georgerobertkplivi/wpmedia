import os

from dotenv import load_dotenv

from pages.wp_login_page import WpLoginPage

# Load environment variables from the .env file
load_dotenv()


class BaseTest(WpLoginPage):
    base_url = "http://test.local/wp-admin/tools.php?page=wpcrawler_admin"

    # Retrieve the values using os.getenv in the constructor
    # username = os.getenv("USERNAME")
    username = "dev-email@wpengine.local"
    # password = os.getenv("PASSWORD")
    password = "qatest"

    def setUp(self):
        super().setUp()
        self.open(self.base_url)
        self.maximize_window()
        self.login_to_wp(self.username, self.password)

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()
