from pages.Base import Base


class Register(Base):

    create_one_button = ('id', 'com.login/module.learning:id/textViewLinkRegister')
    name_input = ('id', 'com.login/module.learning:id/textInputEditTextName')
    email_input = ('id', 'com.login/module.learning:id/textInputEditTextEmail')
    password_input = ('id', 'com.login/module.learning:id/textInputEditTextPassword')
    password_confirmation_input = ('id', 'com.login/module.learning:id/textInputEditTextConfirmPassword')

    def click_create_one_button(self):
        self.send_keys(self.create_one_button, "")

    def enter_name(self):

        self.send_keys(self.name_input, "ttest")

    def enter_email(self):

        self.send_keys(self.email_input, "TestAccount@gmail.com")

    def enter_password(self):

        self.send_keys(self.password_input, "xyz123")

    def enter_password_confirmation(self):

        self.send_keys(self.password_confirmation_input, "xyz123")
