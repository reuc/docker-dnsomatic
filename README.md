
Docker DNS-O-Matic
==================

Easily announce your new IP address to the world.

Installation
------------

Builds of the image are available on [Docker Hub](https://hub.docker.com/r/reuc/dnsomatic/) where you can download from the latest stable image.

    docker pull codeworksio/dnsomatic

Alternatively you can build the image yourself.

    docker build --tag codeworksio/dnsomatic \
        github.com/codeworksio/docker-dnsomatic

Quickstart
----------

Start container using:

    docker run --detach --restart always \
        --name dnsomatic \
        --hostname dnsomatic \
        --env "DNSOMATIC_USERNAME=username" \
        --env "DNSOMATIC_PASSWORD=password" \
        --env "DNSOMATIC_HOSTNAME=fqdn" \
        codeworksio/dnsomatic

See
---

* [DNS-O-Matic API](https://www.dnsomatic.com/wiki/api)
