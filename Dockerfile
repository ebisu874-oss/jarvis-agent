FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

RUN uv pip install --system "mistralai-agents>=1.1.0"

COPY . .

CMD ["agents", "serve"]