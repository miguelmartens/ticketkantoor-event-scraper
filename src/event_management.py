from .logging_utils import configure_logging
import logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Configure logging for this module
configure_logging()
logger = logging.getLogger(__name__)

def select_event(driver, event_name):
    """
    Selects an event on a web page using the provided WebDriver and event name.

    Args:
        driver (webdriver): Selenium WebDriver instance used for web page interaction.
        event_name (str): Name of the event to select.

    Raises:
        Exception: If the event selection fails.
    """
    try:
        logger.info(f"Selecting event: {event_name}")
        event_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'eventdropdown')))
        select = Select(event_dropdown)
        select.select_by_visible_text(event_name)
        logger.info(f"Event selected successfully: {event_name}")
    except (NoSuchElementException, TimeoutException) as e:
        logger.error(f"Event selection failed: {e}")
        raise

def extract_data(driver):
    """
    Extracts data from a web page using the provided WebDriver.

    Args:
        driver (webdriver): Selenium WebDriver instance used for web page interaction.

    Returns:
        str: The extracted data text.

    Raises:
        Exception: If data extraction fails.
    """
    try:
        logger.info("Extracting data from event page")
        data_div = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@style, 'text-align:center') and contains(@style, 'font-size:25px')]"))
        )
        data = data_div.text
        logger.info("Data extracted successfully")
        return data
    except (NoSuchElementException, TimeoutException) as e:
        logger.error(f"Data extraction failed: {e}")
        raise
