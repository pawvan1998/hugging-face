Tag  Docker Image: Tag  Docker image with  Docker Hub username and a repository name. This allows you to push the image to Docker Hub.

docker tag huggingface-report pawvan1998/huggingface-report:latest

 Push tagged Docker image to Docker Hub.

docker push pawvan1998/huggingface-report:latest
Pull and Run the Docker Container: On any Linux machine with Docker installed
users can easily pull your Docker image from Docker Hub and run it using the following commands:

docker pull pawvan1998/huggingface-report:latest
docker run --rm pawvan1998/huggingface-report:latest

