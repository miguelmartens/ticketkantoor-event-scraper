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
  git clone https://github.com/your-repository/ticketkantoor-event-scraper.git
  ```

2. Navigate to the project directory:
  ```bash
  cd ticketkantoor-event-scraper
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
docker build -t ticketkantoor-event-scraper .
```

And run it with:

```bash
docker run -e TICKETKANTOOR_EMAIL=your_email -e TICKETKANTOOR_PASSWORD=your_password -e GRAPH_API_CLIENT_ID=your_client_id -e GRAPH_API_CLIENT_SECRET=your_client_secret -e GRAPH_API_TENANT_ID=your_tenant_id -e USER_OBJECT_ID=your_user_object_id -e RECIPIENT_EMAIL=your_recipient_email -e USE_EMAIL_UTILS=true -e EVENT_NAME="Your Event Name" ticketkantoor-event-scraper
```

Remember to replace your_email, your_password, your_client_id, your_client_secret, your_tenant_id, your_user_object_id, your_recipient_email, and "Your Event Name" with your actual Ticketkantoor credentials, Microsoft Graph API credentials, and other configuration details.

### Explanation:

1. **Docker Build Command**: This command builds a Docker image named `ticketkantoor-event-scraper` from the Dockerfile in the current directory.

2. **Docker Run Command**: This command runs the container from the built image. It includes setting environment variables using `-e`. These variables should be replaced with actual values for your application to function correctly.

   - `TICKETKANTOOR_EMAIL` and `TICKETKANTOOR_PASSWORD` are for logging into Ticketkantoor.
   - `GRAPH_API_CLIENT_ID`, `GRAPH_API_CLIENT_SECRET`, and `GRAPH_API_TENANT_ID` are for the Microsoft Graph API authentication.
   - `USER_OBJECT_ID` and `RECIPIENT_EMAIL` are for sending emails through the Microsoft Graph API.
   - `USE_EMAIL_UTILS` is a flag to enable or disable email sending functionality.
   - `EVENT_NAME` is the name of the event you're scraping.

This section is critical for users who prefer Docker for deployment, ensuring they have clear instructions on how to containerize and run your application.

## Creating and Pushing Tags for Docker Images
Our project uses semantic versioning for Docker images, which is automated through GitHub Actions. Semantic versioning follows the MAJOR.MINOR.PATCH format, where:

* MAJOR version is incremented for incompatible API changes,
* MINOR version is incremented for added functionality in a backward-compatible manner,
* PATCH version is incremented for backward-compatible bug fixes.

To create a new version of the Docker image, follow these (example) steps:

1. Create a Tag:
    * Ensure you have committed all the changes that should go into the new version.
    * Create a Git tag with the new version number, prefixed with v. For example, for version 1.0.0, use v1.0.0:

    ```bash
    git tag -a v1.0.0 -m "Release version 1.0.0"
    ```

    In the message, include a brief description or changelog of the release.

2. Push the Tag to GitHub:
    * Push the tag to your GitHub repository:

    ```bash
    git push origin v1.0.0
    ```

    * This push will trigger the GitHub Actions workflow, which builds and pushes the Docker image to Docker Hub.

3. View on Docker Hub:
    * Once the GitHub Actions workflow completes, the new Docker image with the tag v1.0.0 will be available on Docker Hub.
    * Additionally, the latest tag on Docker Hub will be updated to this new version.

### Best Practices
* Stable Versions: Users who require stable versions of the Docker image should pull specific versioned tags from Docker Hub.
* Latest Tag: The latest tag is always set to the most recent version. It's convenient but might not always be the most stable.
* Version Consistency: Keep your versioning consistent and in line with the changes made in the code to maintain clarity for the users.

## Contributing
Contributions to this project are welcome. Please ensure you follow the coding standards and write tests for new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
