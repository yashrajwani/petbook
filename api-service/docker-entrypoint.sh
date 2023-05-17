echo "Container is running!!!"
pipenv run uvicorn service:app --host 0.0.0.0 --port 8000 --lifespan on