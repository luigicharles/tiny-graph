# 🧬 tiny-graph
graphql-mongodb-python 

## Requirements

    python >= 3.5
    mongoatlas cluster
    docker-compose (if using with docker)

## Setup

1) Add your mongo cluster uri to the MONGO_URI variable in 

        ./src/config/.mongo.env

2) Install python requirements to an enviroment of your choice: 

        pip3 install -r ./requirements.txt

3) Cd into:

        ./src

4) To start the server locally run the following command: 

        uvicorn main:app

## Docker

A fully configured docker-compose.yml and dockerfile is given in the top level directory. To build and run the container on port 8001 execute in the top level: 

        docker-compose up --build 


## Deploying to GCP 

1) Open the cloudbuild.yaml file and make the following substitutions to your usecase:

        _GCP_PROJECT: '<your-project-name>'
        _GCP_REGION: 'us-east1'
        _GCP_CLOUD_RUN_NAME: 'tiny-graph'
        _DOCKER_IMAGE : 'tiny-graph-image'
        _MAX_INSTANCES: '1'
        _CONCURRENCY: '100'
        _CPUS: '1'
        _MEMORY: '256'

2) Assuming you have the requisite IAM permissions for CloudBuild,CloudRegistry and CloudRun you can then run in the top level:

    gcloud builds submit