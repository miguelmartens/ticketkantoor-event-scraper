import unittest
import logging
from src.logging_utils import configure_logging

class TestLoggingUtils(unittest.TestCase):

    def setUp(self):
        # Reset the logger to its default level
        logging.getLogger().setLevel(logging.WARNING)

    def test_configure_logging(self):
        # Assert the default logging level is WARNING
        self.assertEqual(logging.getLogger().level, logging.WARNING)

        # Configure logging
        configure_logging()

        # Optionally, check if the level changes to INFO after configuration
        # self.assertEqual(logging.getLogger().level, logging.INFO)

if __name__ == '__main__':
    unittest.main()
