import unittest
from unittest.mock import patch, MagicMock
from src.email_utils import send_email_with_graph_api

class TestEmailUtils(unittest.TestCase):

    @patch('src.email_utils.requests.post')
    def test_send_email_with_graph_api_success(self, mock_post):
        # Mocking the response of requests.post for a successful email send
        mock_response = MagicMock()
        mock_response.status_code = 202
        mock_response.json.return_value = {'message': 'Success'}  # Mock successful JSON response
        mock_post.return_value = mock_response

        # Call the function
        status_code = send_email_with_graph_api(
            'access_token', 'recipient@example.com', 'Subject', 'Body', 'user_object_id'
        )

        # Assert the function returns the correct status code
        self.assertEqual(status_code, 202)

    @patch('src.email_utils.requests.post')
    def test_send_email_with_graph_api_failure(self, mock_post):
        # Mocking the response of requests.post for a failed email send
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {'error': 'Failure message'}  # Mock error JSON response
        mock_post.return_value = mock_response

        # Call the function
        status_code = send_email_with_graph_api(
            'access_token', 'recipient@example.com', 'Subject', 'Body', 'user_object_id'
        )

        # Assert the function returns the failure status code
        self.assertNotEqual(status_code, 202)

if __name__ == '__main__':
    unittest.main()
