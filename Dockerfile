FROM alpine:3.9 AS deployment

ENV LANG C.UTF-8

# Python runtime
RUN apk add --no-cache python3
RUN ln -sf /usr/bin/pip3 /usr/bin/pip
RUN ln -sf /usr/bin/python3 /usr/bin/python

# Development runtime
RUN apk add --no-cache --virtual .build-deps build-base python3-dev
RUN pip install pipenv

# Configure package deployment
ENV PYROOT /PYROOT
ENV PATH $PYROOT/bin:$PATH
ENV PYTHONUSERBASE $PYROOT

# Build application
WORKDIR /build
COPY Pipfile Pipfile.lock ./
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy

# Production image
FROM alpine:3.9 AS production

# Python runtime
RUN apk add --no-cache python3
RUN ln -sf /usr/bin/pip3 /usr/bin/pip
RUN ln -sf /usr/bin/python3 /usr/bin/python

ENV PYROOT /PYROOT
ENV PATH $PYROOT/bin:$PATH
ENV PYTHONPATH $PYROOT/lib/python:$PATH
ENV PYTHONUSERBASE $PYROOT

# Copy over deployment artifacts
COPY --from=deployment $PYROOT/lib/ $PYROOT/lib/
COPY . ./

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
