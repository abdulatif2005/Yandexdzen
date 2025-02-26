# Yandexdzen

This project is containerized using Docker and can be easily started with `docker-compose`.

## Prerequisites

Make sure you have the following installed on your system:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone the repository:
   ```sh
   git clone https://github.com/abdulatif2005/Yandexdzen.git
   cd Yandexdzen
   ```


2. Build and start the containers:
   ```sh
   docker-compose build
   docker-compose up -d
   ```
   This will build and start the project.


3. To check running containers:
   ```sh
   docker ps
   ```

4. To stop the containers:
   ```sh
   docker-compose down
   ```

## Additional Commands

- View logs:
  ```sh
  docker-compose logs -f
  ```
- Restart containers:
  ```sh
  docker-compose restart
  ```