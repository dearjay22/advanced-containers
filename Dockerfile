# ==============================
# Stage 1 — Build dependencies
# ==============================
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies for compiling Python packages (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements first (to leverage Docker cache)
COPY requirements.txt ./

# Install Python dependencies into a user-local directory
RUN pip install --user --no-cache-dir -r requirements.txt


# ==============================
# Stage 2 — Runtime
# ==============================
FROM python:3.11-slim

# Create a non-root user
RUN useradd -m appuser

# Switch to non-root user
USER appuser

WORKDIR /home/appuser/app

# Copy installed dependencies from builder stage
COPY --from=builder /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

# Copy source code
COPY --chown=appuser:appuser . .

# Expose Flask port
EXPOSE 5000

# Environment variables
ENV FLASK_APP=app.main
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Command to run the app
CMD ["flask", "run"]
