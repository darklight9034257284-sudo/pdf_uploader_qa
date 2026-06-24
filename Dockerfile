# Use an official lightweight Python image
FROM python:3.14-slim

# Set the working directory inside the container
WORKDIR /app

# Install build tools needed for simpleaudio and other C extensions
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache layers
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir \
    torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose Streamlit's default network port
EXPOSE 8501

# Configure Streamlit health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run Streamlit with production-ready flags
ENTRYPOINT ["sh", "-c", "streamlit run llm.py --server.address=0.0.0.0 --server.port=${PORT:-8501}"]
