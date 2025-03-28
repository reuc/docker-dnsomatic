FROM reuc/docker-ubuntu

ENV DNSOMATIC_USERNAME="username" \
    DNSOMATIC_PASSWORD="password" \
    DNSOMATIC_DELAY="60" \
    DNSOMATIC_INTERVAL="60" \
    DNSOMATIC_TRIES="0" \
    DNSOMATIC_HOSTNAME="fqdn"

RUN set -ex; \
    pip install \
        pytz \
        requests --break-system-packages

COPY assets/ /

CMD [ "python3", "-u", "/usr/local/bin/dnsomatic.py" ]

### METADATA ###################################################################

ARG IMAGE
ARG BUILD_DATE
ARG VERSION
ARG VCS_REF
ARG VCS_URL
LABEL \
    org.label-schema.name=$IMAGE \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.version=$VERSION \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url=$VCS_URL \
    org.label-schema.schema-version="1.0"
