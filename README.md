# Meet Dapp - Decentralized Meeting Application

This is a decentralized application (Dapp) called "Meet Dapp" that enables users to organize meetings in a decentralized manner. The application operates on a decentralized network and utilizes blockchain technology for secure and transparent meeting management.

## Getting Started:

### Step 1: Build Docker Image

Run the following command to build the Docker image for the decentralized application:

```console
docker build -t meetdapp:latest .
```

### Step 2: Run the Application

```console 
docker run -p 8080:80 -v "$(pwd)":/code -it meetdapp:latest 
```
The application will be available in your web browser at http://localhost:8080

Each time you change your code the server will restart automatically!

### API Documentation

The decentralized meeting application's API is documented with Swagger. You can access the documentation in your web browser through the following link:

- Swagger **(Interactive)**: http://localhost:8080/docs
- Redoc: http://localhost:8080/redoc

Thank you for using Meet Dapp! If you have any questions or need assistance, feel free to reach out to us.