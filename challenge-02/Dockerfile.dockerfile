# Use the official Golang image as the base image
FROM golang:1.18-alpine

# Set the current working directory inside the container
WORKDIR /app

# Copy the Go module files and the source code into the container
COPY golang/server.go ./
COPY golang/file.txt ./file.txt
COPY golang/file-dev.txt ./file-dev.txt
COPY golang/file-prod.txt ./file-prod.txt

# Build the Go application
RUN go build -o server server.go

# Command to run the web server
CMD ["./server"]
