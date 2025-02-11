#!/bin/bash

set -euo pipefail

if ! docker compose ps --services --filter "status=running" | grep -q "app"; then
    docker compose up -d --build app
fi

docker compose exec app "$@"
