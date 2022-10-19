FROM alpine:3.8
RUN apk update
RUN apk add --no-cache nodejs
RUN apk add --no-cache curl
COPY . /app
# CMD ["/usr/bin/node", "/app/app.js"]
# EXPOSE 8080/tcp