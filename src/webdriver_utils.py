from selenium import webdriver
import logging

def initialize_driver():
    """
    Initializes and returns a Selenium WebDriver with Chrome options.

    The driver is configured to run headless and with various options for stability and performance.
    A custom user agent is set for the driver.

    Returns:
        webdriver.Chrome: An instance of Chrome WebDriver with specified options.
    """
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('window-size=1920x1080')

        return webdriver.Chrome(options=options)
    except Exception as e:
        logging.error(f"Error initializing WebDriver: {e}")
        raise
