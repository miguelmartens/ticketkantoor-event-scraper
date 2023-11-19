import unittest
import importlib
from unittest.mock import patch
from src import config

class TestConfig(unittest.TestCase):

    def setUp(self):
        # Set up a patcher to mock environment variables
        self.env_patcher = patch.dict('os.environ', {
            'TICKETKANTOOR_EMAIL': 'default_email@example.com',
            'TICKETKANTOOR_PASSWORD': 'default_password',
            'GRAPH_API_CLIENT_ID': 'default_client_id',
            'GRAPH_API_CLIENT_SECRET': 'default_client_secret',
            'GRAPH_API_TENANT_ID': 'default_tenant_id',
            'USER_OBJECT_ID': 'default_user_object_id',
            'RECIPIENT_EMAIL': 'recipient@example.com',
            'USE_EMAIL_UTILS': 'true',
            'EVENT_NAME': 'Default Event Name'
        })
        self.env_patcher.start()

    def tearDown(self):
        # Stop the patcher to reset the environment
        self.env_patcher.stop()

    def test_config_variables(self):
        # Test if the configuration variables are set correctly
        self.assertEqual(config.TICKETKANTOOR_EMAIL, 'default_email@example.com')
        self.assertEqual(config.TICKETKANTOOR_PASSWORD, 'default_password')
        # Add assertions for other config variables

    def test_use_email_utils_flag(self):
        # Reload config module to apply the mocked environment variables
        importlib.reload(config)

        # Test if the USE_EMAIL_UTILS flag is interpreted correctly
        self.assertTrue(config.USE_EMAIL_UTILS)

if __name__ == '__main__':
    unittest.main()
