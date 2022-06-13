FROM python:3.7
RUN python -m pip install flask


EXPOSE 8080
COPY /app /app
WORKDIR /app
CMD ["python", "app.py"]
