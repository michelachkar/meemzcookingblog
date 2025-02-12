# pull official base image
FROM python:3.11

# Set working directory inside the container
WORKDIR /my_site

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    default-libmysqlclient-dev \
    libpq-dev \
    pkg-config \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Ensure pip is up to date
RUN python -m pip install --upgrade pip

# Copy requirements first to cache dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .


# Make sure entrypoint.sh has executable permissions
RUN chmod +x entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Run the entrypoint script
ENTRYPOINT ["/bin/sh", "entrypoint.sh"]

# Default command to start Django with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_site.wsgi:application"]
