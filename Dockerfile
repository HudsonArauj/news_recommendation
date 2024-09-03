FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN pip install --no-cache-dir pytest && pytest --disable-warnings
    
EXPOSE 6599

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "6599"]