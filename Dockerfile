FROM python:3.7
RUN pip3 install Flask netifaces


EXPOSE 8080
COPY /app /app

ENTRYPOINT ["/usr/bin/python3", "/app/app.py"]
