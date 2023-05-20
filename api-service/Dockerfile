FROM python:3.9-slim-buster

# Tell pipenv where the shell is. This allows us to use "pipenv shell" as a
# container entry point.

# Python wants UTF-8 locale
ENV LANG=C.UTF-8

WORKDIR /app

ENV PYENV_SHELL=/bin/bash
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY Pipfile Pipfile.lock .


RUN pip install pipenv && \
    pipenv sync
    
# RUN pipenv run pip install zipfile && \
#     pipenv run pip install tarfile && \
#     pipenv run pip install torch

RUN pipenv run pip install torch
COPY ./api ./docker-entrypoint.sh .

RUN pipenv run pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000

ENTRYPOINT ["/bin/bash","./docker-entrypoint.sh"]
# ENTRYPOINT ["/bin/bash"]
