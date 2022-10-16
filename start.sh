#!/usr/bin/env bash
set -e
echo "start 1b"
mlflow server --host 0.0.0.0 --port 4180 --backend-store-uri ${BACKEND_STORE_URI} --default-artifact-root ${DEFAULT_ARTIFACT_ROOT} &
# mlflow server --host 0.0.0.0 --port 8080 --backend-store-uri ${BACKEND_STORE_URI} --default-artifact-root ${DEFAULT_ARTIFACT_ROOT} &
echo "start 2b: ${BACKEND_STORE_URI}::${DEFAULT_ARTIFACT_ROOT}"
# while ! nc -z localhost 8080 ; do sleep 1 ; done
# echo "start 3"

# /oauth2-proxy/oauth2-proxy --upstream=http://localhost:8080 --config=${OAUTH_PROXY_CONFIG} --http-address=0.0.0.0:4180 &
# echo "start 4"

wait -n



#!/usr/bin/env bash
# set -e
# echo "start 1"
# mlflow server --host 0.0.0.0 --port 8080 --backend-store-uri ${BACKEND_STORE_URI} --default-artifact-root ${DEFAULT_ARTIFACT_ROOT} &
# echo "start 2: ${BACKEND_STORE_URI}::${DEFAULT_ARTIFACT_ROOT}"
# while ! nc -z localhost 8080 ; do sleep 1 ; done
# echo "start 3"

# /oauth2-proxy/oauth2-proxy --upstream=http://localhost:8080 --config=${OAUTH_PROXY_CONFIG} --http-address=0.0.0.0:4180 &
# echo "start 4"

# wait -n
