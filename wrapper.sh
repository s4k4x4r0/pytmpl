#!/bin/bash

set -euo pipefail

BUILD=false
RESTART=false
ARGS=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --build)
            BUILD=true
            shift
            ;;
        --restart)
            RESTART=true
            shift
            ;;
        *)
            ARGS+=("$1")
            shift
            ;;
    esac
done

if [ "$BUILD" = true ]; then
    docker compose up -d --build app
elif [ "$RESTART" = true ]; then
    docker compose restart app
elif ! docker compose ps --services --filter "status=running" | grep -q "app"; then
    docker compose up -d app
fi

if [ ${#ARGS[@]} -gt 0 ]; then
    docker compose exec app "${ARGS[@]}"
fi
