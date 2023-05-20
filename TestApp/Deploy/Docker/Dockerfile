FROM python:3.10.4

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN mkdir /config
COPY ./requirements.txt /config/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /config/requirements.txt

COPY ./app /app
COPY ./app/Untitled-5.pdf /Untitled-5.pdf

COPY ./entrypoint.sh /app/entrypoint.sh
RUN ["chmod", "+x", "/app/entrypoint.sh"]

ENTRYPOINT ["/app/entrypoint.sh"]