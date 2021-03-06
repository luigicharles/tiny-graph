FROM tiangolo/uvicorn-gunicorn-starlette:python3.7

# Copy Source Code to Container
COPY ./src /app

# Copy Python Requirements
COPY ./requirements.txt ./app/requirements.txt

# Change Working Directory
WORKDIR /app

# Install Python Requirements
RUN pip3 install -r ./app/requirements.txt