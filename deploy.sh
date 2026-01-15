#!/usr/bin/env bash
set -euo pipefail

# Déploiement "simple" sur VPS:
# - récupère le dernier code
# - rebuild l'image
# - redémarre le service

git pull origin main
docker compose up -d --build
