FROM python:3.7
RUN  python --version

# Create app directory
WORKDIR /app

# # copy requirements.txt
# COPY local-src/requirements.txt ./

RUN apt-get update
RUN apt-get install default-jdk -y

# Install app dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Flask application when the container starts
CMD ["python", "app.py"]