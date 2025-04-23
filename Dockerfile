# ビルドステージ

FROM ghcr.io/astral-sh/uv:0.6.16-python3.13-bookworm-slim AS uv

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

# 実行ステージ

FROM python:3.13-slim

WORKDIR /app

COPY --from=uv --chown=app:app /app /app

ENTRYPOINT ["/app/.venv/bin/python"]

