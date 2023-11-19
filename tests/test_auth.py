import unittest
from unittest.mock import patch, MagicMock
from src.auth import login, get_access_token

class TestAuth(unittest.TestCase):

    @patch('src.auth.requests.post')
    def test_get_access_token(self, mock_post):
        # Mocking the response of requests.post
        mock_response = MagicMock()
        mock_response.json.return_value = {'access_token': 'test_token'}
        mock_post.return_value = mock_response

        # Call the function
        token = get_access_token('client_id', 'client_secret', 'tenant_id')

        # Assert token is returned as expected
        self.assertEqual(token, 'test_token')
        mock_post.assert_called_once()

    @patch('src.auth.WebDriverWait')
    @patch('selenium.webdriver.Chrome')  # Corrected patching reference
    def test_login(self, mock_chrome, mock_wait):
        # Mock the Chrome driver and its methods
        mock_driver_instance = mock_chrome.return_value
        mock_driver_instance.find_element.return_value = MagicMock()

        # Mock WebDriverWait
        mock_wait.until.return_value = MagicMock()

        # Call the function
        login(mock_driver_instance, 'test@email.com', 'test_password')

        # Assertions
        self.assertTrue(mock_driver_instance.find_element.called)
        # Add more assertions as needed

if __name__ == '__main__':
    unittest.main()
