# Create app directory and set permissions
RUN mkdir /app && chmod 777 /app
WORKDIR /app

# Install system dependencies in a single layer
RUN apt-get update -qq --fix-missing && \
    apt-get install -y --no-install-recommends \
    git \
    wget \
    zstd \
    p7zip \
    ffmpeg \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --upgrade pip

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

CMD ["bash", "start.sh"]
