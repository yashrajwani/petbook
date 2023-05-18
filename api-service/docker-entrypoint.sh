echo "Container is running!!!"
pipenv run uvicorn service:app --port 8000 --lifespan on