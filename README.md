# Ticketkantoor Event Scraper

## Introduction
This project is a Python-based scraper for extracting event data from the Ticketkantoor website. It uses Selenium for web scraping, sends results via Microsoft Graph API, and is configurable through environment variables.

## Features
- Web scraping with Selenium WebDriver.
- Authentication and data extraction for specific events on Ticketkantoor.
- Email notification of extracted data using Microsoft Graph API.
- Configurable settings through environment variables.

## Installation
To set up this project:

1. Clone the repository:
  ```bash
  git clone https://github.com/your-repository/ticketkantoor-scraper.git
  ```

2. Navigate to the project directory:
  ```bash
  cd ticketkantoor-scraper
  ```

3. (Optional) Set up a virtual environment:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
  ```

4. Install the requirements:
  ```bash
  pip3 install --no-cache-dir -r requirements.txt
  ```

## Configuration
Configure the application settings via environment variables. The required environment variables include:

* TICKETKANTOOR_EMAIL: Email for Ticketkantoor login.
* TICKETKANTOOR_PASSWORD: Password for Ticketkantoor login.
* GRAPH_API_CLIENT_ID: Client ID for Microsoft Graph API.
* GRAPH_API_CLIENT_SECRET: Client Secret for Microsoft Graph API.
* GRAPH_API_TENANT_ID: Tenant ID for Microsoft Graph API.
* USER_OBJECT_ID: Object ID of the user in Microsoft Graph API.
* RECIPIENT_EMAIL: Email address to send the extracted data to.
* USE_EMAIL_UTILS: Set to true to enable email sending.
* EVENT_NAME: Name of the event to scrape data for.

Set these variables in your environment or a .env file.

## Usage
Run the script with:

```bash
python main.py
```

## Docker Usage
If you are using Docker, build the container with:

```bash
docker build -t ticketkantoor-scraper .
```

And run it with:

```bash
docker run -e TICKETKANTOOR_EMAIL=your_email -e TICKETKANTOOR_PASSWORD=your_password -e GRAPH_API_CLIENT_ID=your_client_id -e GRAPH_API_CLIENT_SECRET=your_client_secret -e GRAPH_API_TENANT_ID=your_tenant_id -e USER_OBJECT_ID=your_user_object_id -e RECIPIENT_EMAIL=your_recipient_email -e USE_EMAIL_UTILS=true -e EVENT_NAME="Your Event Name" ticketkantoor-scraper
```

Remember to replace your_email, your_password, your_client_id, your_client_secret, your_tenant_id, your_user_object_id, your_recipient_email, and "Your Event Name" with your actual Ticketkantoor credentials, Microsoft Graph API credentials, and other configuration details.

### Explanation:

1. **Docker Build Command**: This command builds a Docker image named `ticketkantoor-scraper` from the Dockerfile in the current directory.

2. **Docker Run Command**: This command runs the container from the built image. It includes setting environment variables using `-e`. These variables should be replaced with actual values for your application to function correctly.

   - `TICKETKANTOOR_EMAIL` and `TICKETKANTOOR_PASSWORD` are for logging into Ticketkantoor.
   - `GRAPH_API_CLIENT_ID`, `GRAPH_API_CLIENT_SECRET`, and `GRAPH_API_TENANT_ID` are for the Microsoft Graph API authentication.
   - `USER_OBJECT_ID` and `RECIPIENT_EMAIL` are for sending emails through the Microsoft Graph API.
   - `USE_EMAIL_UTILS` is a flag to enable or disable email sending functionality.
   - `EVENT_NAME` is the name of the event you're scraping.

This section is critical for users who prefer Docker for deployment, ensuring they have clear instructions on how to containerize and run your application.

## Contributing
Contributions to this project are welcome. Please ensure you follow the coding standards and write tests for new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
