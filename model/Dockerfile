# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install system-level dependencies
RUN yum update -y && yum install -y \
    && yum clean all

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set up the command to run scripts (you can override this)
CMD ["bash"]
