#!/usr/bin/env bash
# Fetches the public GCOM OpenAPI spec and reports whether it differs from the
# committed copy. Writes drift=true|false to $GITHUB_OUTPUT (if set).
set -euo pipefail

OPENAPI_URL="https://grafana.com/api/openapi.json"
SPEC_PATH="openapi/gcom.openapi.json"
FRESH_SPEC="${FRESH_SPEC:-/tmp/gcom-openapi-fresh.json}"
OUTPUT="${GITHUB_OUTPUT:-/dev/stdout}"

curl -fsSL "${OPENAPI_URL}" -o "${FRESH_SPEC}"

# The public spec is unauthenticated; confirm we did not receive anything else.
if [ "$(jq -r '.info.version' "${FRESH_SPEC}")" != "public" ]; then
  echo "Unexpected spec received: info.version is not 'public'." >&2
  exit 1
fi

normalize() {
  jq -S -c 'del(.info."x-commit-sha", .info."x-generated-at")' "$1"
}

if [ -f "${SPEC_PATH}" ] && [ "$(normalize "${SPEC_PATH}")" = "$(normalize "${FRESH_SPEC}")" ]; then
  echo "No OpenAPI drift detected."
  echo "drift=false" >> "${OUTPUT}"
  exit 0
fi

echo "OpenAPI drift detected."
echo "drift=true" >> "${OUTPUT}"
