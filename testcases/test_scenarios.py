import json
import os

import pytest
from pages.login_page import LoginPage
from utilities.utility import *


def load_test_data(file_path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, file_path)
    with open(full_path, 'r') as file:
        return json.load(file)


@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_login_fields(self):
        # check username field appears
        username_field = get_textfield_by_id(self.wait, "user-name")
        assert username_field is not None, "username field not found"

        # check password field appears
        password_field = get_textfield_by_id(self.wait, "password")
        assert password_field is not None, "password field not found"

        # check login button appears and clickable
        login_btn = get_clickable_btn_by_id(self.wait, "login-button")
        assert login_btn is not None, "Login button should be found and clickable"

    @pytest.mark.parametrize("credentials", load_test_data("../testdata/valid_credentials.json").values())
    def test_valid_credentials(self, credentials):
        username = credentials["username"]
        password = credentials["password"]
        # Login with valid credentials
        login_page = LoginPage(self.wait)
        login_page.login(username, password)

        # check login successfully by reaching home page
        text = get_text_in_div(self.wait, "Swag Labs")
        assert text is not None, "text 'Swag Labs' not found"

    @pytest.mark.parametrize("credentials", load_test_data("../testdata/wrong_credentials.json").values())
    def test_wrong_credentials(self, credentials):
        username = credentials["username"]
        password = credentials["password"]

        # Login with valid credentials
        login_page = LoginPage(self.wait)
        login_page.login(username, password)

        # check the home page is not reached
        text = get_text_in_div(self.wait, "Products")
        assert text is None, "should have not reached the home page"

        # check the error message appeared
        error_message = get_element_by_class(self.wait,"div.error-message-container.error").text
        assert "Epic sadface: Username and password do not match any user in this service" in error_message

    @pytest.mark.parametrize("credentials", load_test_data("../testdata/empty_credentials.json").values())
    def test_empty_credentials(self, credentials):
        username = credentials["username"]
        password = credentials["password"]

        # Login with valid credentials
        login_page = LoginPage(self.wait)
        login_page.login(username, password)

        # check the home page is not reached
        text = get_text_in_div(self.wait, "Products")
        assert text is None, "should have not reached the home page"

        if username == "":
            # check the error message appeared
            error_message = get_element_by_class(self.wait,"div.error-message-container.error").text
            assert "Epic sadface: Username is required" in error_message
        else:
            # check the error message appeared
            error_message = get_element_by_class(self.wait, "div.error-message-container.error").text
            assert "Epic sadface: Password is required" in error_message
