FROM python:3.10.3-slim

RUN mkdir Statistics
WORKDIR /Statistics

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]