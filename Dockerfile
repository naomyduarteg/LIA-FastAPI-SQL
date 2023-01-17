FROM python:3.10

# Set working directory
WORKDIR /app


COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./main.py /app/
COPY ./sql_app.db /app/sql_app

# Run the application
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]