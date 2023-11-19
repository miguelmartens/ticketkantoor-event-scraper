import unittest
from unittest.mock import patch, MagicMock
from src.event_management import select_event, extract_data

class TestEventManagement(unittest.TestCase):

    @patch('src.event_management.WebDriverWait')
    @patch('src.event_management.Select')
    def test_select_event(self, mock_select, mock_wait):
        # Mocking the WebDriverWait to return a web element with a tag_name of 'select'
        mock_element = MagicMock()
        mock_element.tag_name = 'select'
        mock_wait.return_value.until.return_value = mock_element

        # Mock WebDriver instance
        mock_driver = MagicMock()

        # Set up the mock for Select
        mock_select.return_value = MagicMock()

        # Call the function
        select_event(mock_driver, 'Event Name')

        # Assertions
        mock_select.assert_called_with(mock_element)
        mock_select.return_value.select_by_visible_text.assert_called_with('Event Name')

    @patch('src.event_management.WebDriverWait')
    def test_extract_data(self, mock_wait):
        # Mocking WebDriverWait
        mock_element = MagicMock()
        mock_element.text = 'Extracted Data'
        mock_wait.return_value.until.return_value = mock_element

        # Mock WebDriver instance
        mock_driver = MagicMock()

        # Call the function
        data = extract_data(mock_driver)

        # Assertions
        self.assertEqual(data, 'Extracted Data')

if __name__ == '__main__':
    unittest.main()
