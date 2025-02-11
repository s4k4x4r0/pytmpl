FROM debian:bookworm-slim

COPY --from=ghcr.io/astral-sh/uv:0.5.30 /uv /uvx /bin/

WORKDIR /app
COPY . .

RUN uv sync --frozen
