
Docker DNS-O-Matic
==================

Easily announce your new IP address to the world.

Installation
------------

Builds of the image are available on [Docker Hub](https://hub.docker.com/r/reuc/dnsomatic/) where you can download from the latest stable image.

    docker pull reuc/dnsomatic

Alternatively you can build the image yourself.

    docker build --tag reuc/dnsomatic \
        github.com/reuc/docker-dnsomatic

Quickstart
----------

Start container using:

    docker run --detach --restart always \
        --name dnsomatic \
        --hostname dnsomatic \
        --env "DNSOMATIC_USERNAME=username" \
        --env "DNSOMATIC_PASSWORD=password" \
        --env "DNSOMATIC_HOSTNAME=fqdn" \
        reuc/dnsomatic

See
---

* [DNS-O-Matic API](https://www.dnsomatic.com/wiki/api)
