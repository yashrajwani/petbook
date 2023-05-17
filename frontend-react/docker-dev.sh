docker build -f Dockerfile.dev -t petbook-frontend-dev .

# docker run --rm --name petbook:frontend -ti --mount type=bind,source="$(pwd)",target=/app -p 3000:3000 $IMAGE_NAME
docker run -it --rm -v ${pwd}:/app -v /app/node_modules -p 3000:3000 petbook-frontend-dev