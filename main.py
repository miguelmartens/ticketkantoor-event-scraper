import logging
import sys
from src.webdriver_utils import initialize_driver
from src.auth import login, get_access_token
from src.event_management import select_event, extract_data
from src.email_utils import send_email_with_graph_api
from src.logging_utils import configure_logging
from src.config import (TICKETKANTOOR_EMAIL, TICKETKANTOOR_PASSWORD, GRAPH_API_CLIENT_ID,
                        GRAPH_API_CLIENT_SECRET, GRAPH_API_TENANT_ID, USER_OBJECT_ID,
                        RECIPIENT_EMAIL, USE_EMAIL_UTILS, EVENT_NAME)

# Configure logging for the entire application
configure_logging()

def main():
    try:
        driver = initialize_driver()

        if not all([TICKETKANTOOR_EMAIL, TICKETKANTOOR_PASSWORD]):
            logging.error("Email or password environment variables not set.")
            sys.exit(1)

        login(driver, TICKETKANTOOR_EMAIL, TICKETKANTOOR_PASSWORD)
        select_event(driver, EVENT_NAME)
        data = extract_data(driver)

        if not data:
            logging.error("No data extracted from the event.")
            sys.exit(1)

        logging.info(f"Extracted Data: {data}")

        if USE_EMAIL_UTILS:
            logging.info("USE_EMAIL_UTILS is set to true. Preparing to send email...")
            
            if not all([GRAPH_API_CLIENT_ID, GRAPH_API_CLIENT_SECRET, GRAPH_API_TENANT_ID, USER_OBJECT_ID, RECIPIENT_EMAIL]):
                logging.error("One or more email-related environment variables are not set.")
                sys.exit(1)

            access_token = get_access_token(GRAPH_API_CLIENT_ID, GRAPH_API_CLIENT_SECRET, GRAPH_API_TENANT_ID)
            subject = "Data from Ticketkantoor"
            body = data

            status_code = send_email_with_graph_api(access_token, RECIPIENT_EMAIL, subject, body, USER_OBJECT_ID)

            if status_code == 202:
                logging.info("Email sent successfully via Microsoft Graph API")
            else:
                logging.error(f"Failed to send email. Status code: {status_code}")
        else:
            logging.info("USE_EMAIL_UTILS is set to False. Skipping email sending.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()
