# Use a specific version of selenium/standalone-chrome for predictable builds
FROM selenium/standalone-chrome:119.0-20231122

# Switch to root user to install packages and add a new user
USER root

# Update the system and install Python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create a new user 'appuser' with home directory set to /home/seluser
# This aligns with the directory structure used by the selenium/standalone-chrome image
RUN useradd -m -d /home/seluser appuser

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code from your host to your image filesystem
COPY . .

# Create the Selenium cache directory and set permissions
RUN mkdir -p /home/seluser/.cache/selenium \
    && chown -R appuser:appuser /home/seluser /usr/src/app

# Switch to the new non-root user for running the application
USER appuser

# Run tests
RUN python3 -m unittest discover tests

# Run the Python application on container startup
CMD ["python3", "./main.py"]
