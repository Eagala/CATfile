from pages import Pages
from unittest import TestCase


class TestLoginPage(TestCase):
    email_input = ('id', 'com.login/module.learning:id/textInputEditTextEmail')
    password_input = ('id', 'com.login/module.learning:id/textInputEditTextPassword')
    login_button = ('id', 'com.login/module.learning:id/appCompatButtonLogin')

    def test_enter_email(self):

        Pages.send_keys(self.email_input, "TestAccount@gmail.com")

    def test_enter_password(self):

        Pages.send_keys(self.password_input, "TestAccount@gmail.com")

    def test_enter_login_button(self):

        Pages.click(self.login_button)
