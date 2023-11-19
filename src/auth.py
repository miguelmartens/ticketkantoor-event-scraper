import logging
import requests
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlencode

logger = logging.getLogger(__name__)

def login(driver, email, password):
    """
    Logs into a website using the provided Selenium WebDriver, email, and password.

    Args:
        driver (webdriver): Selenium WebDriver instance used for web interaction.
        email (str): Email address used for login.
        password (str): Password used for login.

    Raises:
        Exception: If login fails.
    """
    try:
        logger.info("Attempting to log in")
        driver.get('https://www.ticketkantoor.nl')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@title="Inloggen en naar je evenementen"]'))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'username'))).send_keys(email)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        logger.info("Login successful")
    except Exception as e:
        logger.error(f"Login failed: {e}")
        raise

def get_access_token(client_id, client_secret, tenant_id):
    """
    Retrieves an access token for Microsoft Graph API using client credentials.

    Args:
        client_id (str): The client ID for the Microsoft Graph API.
        client_secret (str): The client secret for the Microsoft Graph API.
        tenant_id (str): The tenant ID for the Microsoft Graph API.

    Returns:
        str: The retrieved access token.

    Raises:
        Exception: If token retrieval fails.
    """
    try:
        logger.info("Getting access token")
        url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "client_id": client_id,
            "scope": "https://graph.microsoft.com/.default",
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(url, headers=headers, data=urlencode(data))
        response.raise_for_status()
        access_token = response.json().get("access_token")
        logger.info("Access token retrieved successfully")
        return access_token
    except requests.exceptions.RequestException as e:
        logger.error(f"Error retrieving access token: {e}")
        raise
