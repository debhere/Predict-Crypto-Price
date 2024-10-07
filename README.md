
# Predict Crypto-Currency Price

This project is a Machine Learning implementation to predict the time weighted average price (TWAP) for a crypto currency asset (currently only Bitcoin). The project is deployed on cloud and can be accessed with through https://predict-crypto-price.onrender.com/

## Authors

- [@debhere](https://www.github.com/debhere)


## History

- ver_0.0.1: deployed on Oct 7, 2024. Base model created with prophet trained with 6 months of OHLC data from 1 Jan, 2024 to 30 Sep, 2024 to predict ONLY Bitcoin price.

## Tech Stack

**Server:** Streamlit

**Machine Learning:** Meta Prophet

**Database:** Sql-Server 19


## Dataset

Data collection is a key step in any machine learning initiative. The dataset contains 6 month worth of bitcoin ohlc (open, high, low, close) prices over a granularity of 5 mins. 

In order to do that, the coinbase api https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductcandles is invoked and the data is stored in a local sql-server database.

It is a general ETL (Extract, Transform, Load) methodology where the data is extracted from an external api, transformed as applicable and loaded into the database. 

## Database

As mentioned earlier, the collected data is stored locally into a sql-server database. Refer the sql script to create the database schema. [here](/scripts/database/crypto.sql)

Presently, only one table is created for Bitcoin.

## Requirements

- **python 3.11+**
- **streamlit**
- **sckit-learn**
- **numpy**
- **pandas**
- **pyyaml**
- **joblib**
- **sqlalchemy**
- **fire**
- **prophet**
- **requests**

## Run Locally

Clone the project

```bash
  git clone https://github.com/debhere/Predict-Crypto-Price.git
```

Go to the project directory

```bash
  cd Predict-Crypto-Price
```

Create virtual environment

```bash
  conda create -p venv python=3.11 -y
```

Activate virtual environment

```bash
  conda activate venv\
```


Install dependencies

```bash
  pip install -e .
```

create the database schema in sql server. Refer the script at /scripts/database/crypto.sql


collect the data and insert into the database

```bash
./scripts/data_prep.sh
```

Start the server

```bash
  streamlit run app.py
```

## Description

There are 4 main sections (if you will) for this project:-

- Extract-Transform-Load
- Data pipelne
- Model Implementation
- Streamlit server for front-end

The presentation layer (front-end) is very light-weight at this moment with the solitary aim to grab user input and predict the Bitcoin TWAP price. 

### Model Implementation

*src* contains the primary source code of the entire model implmentation mechanism. The primary components are "data ingestion", "data transformation", "model building", and "model evaluation"

*pipeline* contains the data-pipeline and prediction-pipeline.

*utils* directory comprises of common utility functions that is being referred throughout the project.

The starting point of the "model implemention" module is learn.py where each component is being invoked one by one ie., 

data ingestion -> data transformation -> pipeline creation -> model building -> model evaluation.

The best estimator and data pipeline are saved as pickle files as artifacts.

### Front-End

Front-end is nothing but a playground of the model output. Although the majority of the features are anonymized but still thought to create a light-weight interface to demonstrate the usability.

index.html is the solitary html page here with basic css in place.

### Back-End

The back-end server should be kept light-weight for obvious reasons. app.py is the starting point to run the flask server. Once the server is up and running, user will be able to input data onto the front-end html page. flask server captures and performs the data transformation and prediction by invoking the prediction pipeline module. Thereafter, the prediction is rendered on the same UI.

## Support

For any query or discussion, email debmalya.mondal@outlook.com or send me a message on 

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/debmalyamondal)

