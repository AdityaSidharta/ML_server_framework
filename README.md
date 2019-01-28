# ML_server_framework
General Framework in Deploying ML model as a REST API Service

## Instalation
- `docker` : installation can be found [here](https://docs.docker.com/install/)
- `docker-compose` : installation can be found [here](https://docs.docker.com/compose/install/)

## Usage
```
make docker-compose
```

GET requests will be available at [http://localhost:1234] with the following input:

    - class: [1, 2, 3]
    - sex: [M, F]
    - age: int
    - embarked: ['C', 'S', 'Q']


## Prediction as a Service
The list of problems that I would like to tackle in this projects are

- Reproducibility in the whole pipeline

    The projects should be able to be deployed in different environments without hassle. The whole ML pipeline should be agnostic

- Support Continuous Model Training

    The project should be able to build new model automatically whenever there is a change in the dataset. This trained model should be able to be stored and retrieved easily, to be used by the API to perfrom prediction as a service

- Database Update / Data Integrity

    The project should have a proper database suppport to make sure that the model training will always use the latest data.

- Continuous Development / Building

    The model should be able to trained daily - Supports continous development

- Microservice Framework

    Each components will be decoupled - an update to each microservice should not affect the other services.

- Automated Schema Checking / Data Formatting

    The data will undergo an automated Schema Checking which will be used to make sure that the data is ready for training.

## Plan

The technology stack that we will use in this projects are:

- **Scikit-Learn, pandas, numpy** : Model training
- **Airflow** :  Model building, Workflow Pipeline
- **Postgres DB** : Data Storage, Model Storage
- **Flask** : Restful API
- **Docker** : Containerization, Decoupling different services

## Microservices

### postgres
- **Postgres DB** : Data Storage

### minio
- **minio** : Model and Schema Storage

### deploy
- **Flask** : Perform Prediction as a Service to the end user
perform links to db container, should be able to read, write model to db, should be able to read data from db

### model

- **Pandas, Numpy, Scikit-learn** : Model Training
- **Airflow** : Perform continuous building and deployment

### datafill
- **Airflow** : Perform continuous data update

## Microservice Diagram

Coming Soon