import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.utility import *


class LoginPage:

    def __init__(self, wait):
        self.wait = wait

    def login(self, username, password):

        username_field = get_textfield_by_id(self.wait, "user-name")
        assert username_field is not None, "username field not found"

        password_field = get_textfield_by_id(self.wait, "password")
        assert password_field is not None, "password field not found"

        login_btn = get_clickable_btn_by_id(self.wait, "login-button")
        assert login_btn is not None, "Login button should be found and clickable"

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_btn.click()
