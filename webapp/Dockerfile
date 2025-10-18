# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.11-slim
RUN useradd -m appuser
USER appuser
WORKDIR /home/appuser/app

# Copy installed dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

# Copy app source
COPY --chown=appuser:appuser . .

# Expose port
EXPOSE 5000
CMD ["python", "app.py"]
