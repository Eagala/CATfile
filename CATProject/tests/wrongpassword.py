from pages.Base import Base


class WrongPassword(Base):

    email_input = ('id', 'com.login/module.learning:id/textInputEditTextEmail')
    password_input = ('id', 'com.login/module.learning:id/textInputEditTextPassword')
    login_button = ('id', 'com.login/module.learning:id/appCompatButtonLogin')

    def enter_email(self):

        self.send_keys(self.email_input, "tests@gmail.com")

    def enter_password(self):

        self.send_keys(self.password_input, "xyz123456")

    def enter_login_button(self):

        self.send_keys(self.login_button, "")
