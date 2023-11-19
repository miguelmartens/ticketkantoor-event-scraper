import os

# Fetching environment variables for configuration settings
TICKETKANTOOR_EMAIL = os.getenv('TICKETKANTOOR_EMAIL', 'default_email@example.com')
TICKETKANTOOR_PASSWORD = os.getenv('TICKETKANTOOR_PASSWORD', 'default_password')

GRAPH_API_CLIENT_ID = os.getenv('GRAPH_API_CLIENT_ID', 'default_client_id')
GRAPH_API_CLIENT_SECRET = os.getenv('GRAPH_API_CLIENT_SECRET', 'default_client_secret')
GRAPH_API_TENANT_ID = os.getenv('GRAPH_API_TENANT_ID', 'default_tenant_id')

USER_OBJECT_ID = os.getenv('USER_OBJECT_ID', 'default_user_object_id')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', 'recipient@example.com')

USE_EMAIL_UTILS = os.getenv('USE_EMAIL_UTILS', 'false').lower() == 'true'

# Adding the event name variable
EVENT_NAME = os.getenv('EVENT_NAME', 'Default Event Name')

# You can add additional configuration settings as needed
