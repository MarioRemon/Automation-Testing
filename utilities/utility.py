from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def get_textfield_by_id(wait, id):
    try:
        return wait.until(
            EC.presence_of_element_located((By.ID, id))
        )
    except TimeoutException:
        return None


def get_clickable_btn_by_id(wait, id):
    try:
        return wait.until(
            EC.element_to_be_clickable((By.ID, id))
        )
    except TimeoutException:
        return None


def get_text_in_div(wait, text):
    try:
        return wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '"+text+"')]"))
        )
    except TimeoutException:
        return None


def get_element_by_class(wait, class_name):
    try:
        return wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, class_name))
        )
    except TimeoutException:
        return None
