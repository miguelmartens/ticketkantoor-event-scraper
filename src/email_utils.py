import logging
import requests

logger = logging.getLogger(__name__)

def send_email_with_graph_api(access_token, recipient_email, subject, body, user_object_id):
    """
    Sends an email using the Microsoft Graph API.

    Args:
        access_token (str): OAuth2 access token for authentication with Microsoft Graph API.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body content of the email.
        user_object_id (str): The object ID of the user sending the email.

    Returns:
        int: The status code of the email send request.

    Raises:
        Exception: If the email sending fails.
    """
    try:
        url = f"https://graph.microsoft.com/v1.0/users/{user_object_id}/sendMail"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        json_data = {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": "Text",
                    "content": body
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": recipient_email
                        }
                    }
                ]
            }
        }
        response = requests.post(url, headers=headers, json=json_data)
        if response.status_code != 202:
            logger.error(f"Graph API Error: {response.json()}")
            response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending email: {e}")
        raise
