#base image
FROM artemisfowl004/vid-compress
RUN mkdir ./app
RUN chmod 777 /app
WORKDIR /app
RUN pip3 install --upgrade pip

# Fix the Debian Buster repository issue by switching to archive repositories
RUN sed -i 's|deb.debian.org|archive.debian.org|g' /etc/apt/sources.list && \
    sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list && \
    sed -i '/buster-updates/d' /etc/apt/sources.list

RUN apt -qq update --fix-missing
RUN apt -qq install -y git \
    python3 \
    python3-pip \
    wget \
    zstd \
    p7zip \
    ffmpeg \
    curl
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash","start.sh"]
