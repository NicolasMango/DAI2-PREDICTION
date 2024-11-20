FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV MODEL_PATH=/path/to/modelo.pkl
ENV PREPROCESSOR_PATH=/path/to/preprocesador.pkl

EXPOSE 8001

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "app:app"]
