import unittest
from unittest.mock import patch, MagicMock
from src.webdriver_utils import initialize_driver

class TestWebDriverUtils(unittest.TestCase):

    @patch('src.webdriver_utils.webdriver.Chrome')
    def test_initialize_driver(self, mock_chrome):
        # Mocking Chrome WebDriver
        mock_chrome.return_value = MagicMock()

        # Call the function
        driver = initialize_driver()

        # Assertions
        self.assertIsNotNone(driver)
        mock_chrome.assert_called_once()

        # Here, you can also assert if specific options are set to the WebDriver
        # This depends on your implementation of initialize_driver

if __name__ == '__main__':
    unittest.main()
