echo "Container is running!!!"
pipenv run uvicorn service:app --port 8000 --host 0.0.0.0 --lifespan on --log-level trace --proxy-headers