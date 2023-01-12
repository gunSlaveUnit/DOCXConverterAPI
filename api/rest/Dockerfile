FROM python:3.10.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p usr/src/app/docxconverterapi
WORKDIR /usr/src/app/docxconverterapi

COPY ../.. /usr/src/app/docxconverterapi

RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]