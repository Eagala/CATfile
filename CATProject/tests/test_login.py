import pytest
from pages.pages import Pages


@pytest.mark.usefixtures('driver_setup')
class ValidateLogin:
    def test_user_details(self):
        print("Entered into method")
        login = Pages(self.driver)
        login.email_input()
