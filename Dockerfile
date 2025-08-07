FROM ubuntu:22.04

# 1. Install system Python and essential tools
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    python3.10-venv \
    python3.10-dev \
    build-essential \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Create and activate virtual environment
RUN python3.10 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 3. Set up working directory
WORKDIR /app

# 4. Copy requirements first for caching
COPY app/requirements.txt .

# 5. Install exact pinned versions
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application files
COPY app/ .

# 7. Runtime command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
