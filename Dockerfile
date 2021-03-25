FROM python:2-alpine

# Add Maintainer Info
LABEL maintainer="Sam Zhou <sam@mixmedia.com>"

# Set the Current Working Directory inside the container
WORKDIR /app/mixpanel

RUN pip install mixpanel-api \
   && wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 \
   && chmod +x /usr/local/bin/dumb-init

ENTRYPOINT ["dumb-init", "--"]
