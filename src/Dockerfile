FROM debian:trixie-slim

# Install netcat
RUN apt-get update && apt-get install -y netcat && apt-get clean

EXPOSE 8080

# Simple netcat server that listens on port 8080 and echoes back any received data
CMD ["nc", "-l", "-p", "8080", "-e", "/bin/cat"]
