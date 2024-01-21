ARG PYTHON_VERSION=3.9-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY crowdfunding/ /code/

# ENV SECRET_KEY "afk1eu0h5qp9g96!eyoa!%w74%7e(gwkpie00wpt1c6oj#ffw0"
RUN python manage.py collectstatic --noinput
RUN chmod +x /code/run.sh

EXPOSE 8000

CMD ["/code/run.sh"]
