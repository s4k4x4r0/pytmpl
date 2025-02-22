FROM debian:bookworm-slim

COPY --from=ghcr.io/astral-sh/uv:0.5.30 /uv /uvx /bin/

WORKDIR /app
COPY . .

ENV UV_PROJECT_ENVIRONMENT=/.venv
RUN uv sync --frozen

