FROM python:3.10.7
RUN  python --version

# Create app directory
WORKDIR /app

COPY . /app


RUN apt-get update
RUN apt-get install default-jdk -y

# Install app dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Bundle app source

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Flask application when the container starts
CMD ["python", "app.py"]