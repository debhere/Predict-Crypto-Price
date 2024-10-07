
# Predict Crypto-Currency Price

This project is a Machine Learning implementation to predict the time weighted average price (TWAP) for a crypto currency asset (currently only Bitcoin).

## Authors

- [@debhere](https://www.github.com/debhere)


## Tech Stack

**Server:** Streamlit

**Machine Learning:** Meta Prophet



## Dataset

Data collection is a key step in any machine learning initiative. The dataset contains 6 month worth of bitcoin ohlc (open, high, low, close) prices over a granularity of 5 mins. 

In order to do that, the coinbase api https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductcandles is invoked and stored in a local sql-server database.

It is a general ETL (Extract, Transform, Load) methodology where the data is extracted from an external api, transformed as applicable and loaded into the database. 

## Database

As mentioned, the collected data is stored locally into a sql-server database. Refer the sql script to create the database schema. [here](/scripts/database/crypto.sql)

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

Start the server

```bash
  streamlit run app.py
```

## Description

There are 3 main sections (if you will) of this project:-

- Model Implementation
- Front-End
- Back-end

Since , the primary objective of the project to detect the fradulent credit card transactions, the front-end and back-end are quite light-weight in nature.

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

