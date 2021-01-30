# 🧬 tiny-graph
graphql-mongodb-python 

## Requirements

    python >= 3.5
    mongoatlas cluster

## Setup

1) Add your mongo cluster uri to the MONGO_URI variable in ./src/config/.mongo.env

2) Install python requirements to an enviroment of your choice: 

    pip3 install -r ./requirements.txt

3) CD into ./src

4) Run the following command: 

    uvicorn main:app