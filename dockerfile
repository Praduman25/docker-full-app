# ────────────────────────────
# Stage 1 — Builder
# ────────────────────────────
FROM python:3.11-alpine AS builder

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ────────────────────────────
# Stage 2 — Final
# ────────────────────────────
FROM python:3.11-alpine AS final

WORKDIR /app

# copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# copy app code
COPY . .

# make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]