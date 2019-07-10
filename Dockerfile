# Use the base python 3.7 instances
FROM python:3.7-alpine

# Add source code to the container
ADD . /api
# Set the working directory
WORKDIR /api

# Install Dependencies
RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:application", "--worker-connections", "9"]
EXPOSE 8000
