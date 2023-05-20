docker build -t petbook-backend:v3 -f Dockerfile .

docker run -it --rm -p 8000:8000 petbook-backend:v3
# docker run -p 8000:8000 petbook-backend

# docker run --rm --name petbook:api -ti \
# --mount type=bind,source="$(pwd)",target=/app \
# -p 8000:8000 \