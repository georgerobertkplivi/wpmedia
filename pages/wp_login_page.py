from assertpy import assert_that
from seleniumbase import BaseCase


class WpLoginPage(BaseCase):
    WP_USERNAME_TEXTBOX = "//input[@id='user_login']"
    WP_USER_PASSWORD_TEXTBOX = "//input[@id='user_pass']"
    WP_LOGIN_BUTTON = "//input[@id='wp-submit']"

    def enter_username(self, username):
        self.type(self.WP_USERNAME_TEXTBOX, username)

    def enter_password(self, user_password):
        self.type(self.WP_USER_PASSWORD_TEXTBOX, user_password)

    def click_login_button(self):
        self.click(self.WP_LOGIN_BUTTON)

    def verify_wp_login_page_loads(self):
        self.is_element_present(self.WP_LOGIN_BUTTON)
        self.is_element_present(self.WP_USER_PASSWORD_TEXTBOX)
        self.is_element_present(self.WP_USER_PASSWORD_TEXTBOX)

    def login_to_wp(self, username, password):
        self.verify_wp_login_page_loads()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
