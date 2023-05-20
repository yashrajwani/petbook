docker build -f Dockerfile -t petbook-frontend-prod:v2 .

# docker run --rm --name petbook:frontend -ti --mount type=bind,source="$(pwd)",target=/app -p 3000:3000 $IMAGE_NAME
docker run -it --rm -p 80:80 petbook-frontend-prod:v2