FROM python:3.7
COPY . /app
WORKDIR /app
RUN python -m pip install -r requirements.txt


EXPOSE 8080
RUN python -m pytest tests/unit/ # unittest que lo corre en github
CMD python -m pytest tests/integration && python app.py
