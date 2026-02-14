# Flask App with Docker

A simple Flask web application packaged with Docker for easy deployment.

## Features

- Lightweight Flask web app
- Ready for Docker containerization
- Easy deployment to any Docker-enabled environment
- Modular and easy to extend

## Prerequisites

- [Docker](https://www.docker.com/) installed
- Git installed
- Basic knowledge of Flask and Docker

## Getting Started

Follow these steps to run the Flask app locally or deploy using Docker.

### Step 1: Clone the repository

```bash
git clone https://github.com/shaimocoregames/Insurance_premium_API.git
cd Insurance_premium_API
```

### Step 2: Build the Docker image

```bash
docker build -t shaimocoregames/insurance-api:latest .
```

- This builds the Docker image and tags it as `shaimocoregames/insurance-api:latest`.
- The `.` refers to the current directory containing the Dockerfile.

### Step 3: Run the container locally

```bash
docker run -p 5000:5000 shaimocoregames/insurance-api:latest
```

- The app will be available at [http://localhost:5000](http://localhost:5000).
- The `-p 5000:5000` flag maps the container port 5000 to your local machine port 5000.
- To stop the container, press `Ctrl+C` or run:

```bash
docker ps   # find your container ID
docker stop <container_id>
```

### Step 4: Push the image to Docker Hub (optional)

```bash
docker login
docker push shaimocoregames/insurance-api:latest
```

- Make sure you are logged in with your Docker Hub credentials.
- Others can pull your image using:

```bash
docker pull shaimocoregames/insurance-api:latest
```

## Project Structure

```
.
├── app.py           # Main Flask app
├── requirements.txt # Python dependencies
├── Dockerfile       # Docker configuration
└── README.md        # Project documentation
```

### Step 5: Test the app

Once running, open a browser and navigate to:

```
http://localhost:5000
```
- Can also visit it via given link: https://insurance-premium-api-wrx6.onrender.com/

