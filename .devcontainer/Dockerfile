FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm

COPY --from=ghcr.io/astral-sh/uv:0.6.16 --chown=vscode: /uv /uvx /bin/

RUN sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d \
    && echo "source <(task --completion zsh)" >> /home/vscode/.zshrc