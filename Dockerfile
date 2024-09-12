FROM alpine:latest

# Install dependencies
# RUN apk add sqlite sqlite-utils
# RUN apk add --no-cache sqlite sqlite-utils
RUN apk add --no-cache sqlite --repository http://dl-cdn.alpinelinux.org/alpine/v3.20/main

# Copy your application code
COPY . /app

# Set the working directory
WORKDIR /app

# Expose the port for your application (if necessary)
EXPOSE 8501

# Define the command to run your application
CMD ["sqlite3", "semantic_search.db"]