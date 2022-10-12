# Image:version
FROM python:3.10

WORKDIR /home/app

# Create a folder in docker
RUN mkdir -p /home/app

# Copy requirements
COPY ./requirements.txt /home/app/requirements.txt

# Install requirements
RUN pip install --no-cache-dir --upgrade -r /home/app/requirements.txt

# Copy the app in docker
COPY ./src /home/app

# Exposed a port
EXPOSE 8000

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]