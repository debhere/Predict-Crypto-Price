
# Predict Crypto-Currency Price

This project is a Machine Learning implementation to predict the time weighted average price (TWAP) for a crypto currency asset (currently only Bitcoin). The project is deployed on cloud and can be accessed with through https://predict-crypto-price.onrender.com/

## Authors

- [@debhere](https://www.github.com/debhere)


## History

- ver_0.0.1: deployed on Oct 7, 2024. Base model created with facebook prophet trained with 9 months (6 Oct, 2024) of OHLC data from 1 Jan, 2024 to 6 Oct, 2024 to predict ONLY Bitcoin price.

## Tech Stack

**Server:** Streamlit

**Languages:** Python, T-SQL, Bash Script

**Machine Learning:** Meta Prophet

**Database:** Sql-Server 19


## Dataset

Data collection is a key step in any machine learning initiative. The dataset contains 9 month (till Oct 6, 2024) worth of bitcoin ohlc (open, high, low, close) prices over a granularity of 5 mins. 

In order to do that, the coinbase api https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductcandles is invoked and the data is stored in a local sql-server database.

It is a general ETL (Extract, Transform, Load) methodology where the data is extracted from an external api, transformed as applicable and loaded into the database. 

## Database

As mentioned earlier, the collected data is stored locally into a sql-server database. Refer the sql script [here](/scripts/database/crypto.sql) to create the database schema.

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

There are 3 main sections (if you will) for this project:-

- Extract-Transform-Load
- Model Implementation & Pipeline
- Streamlit server for front-end

The presentation layer (front-end) is very light-weight at this moment with the solitary aim to grab user input and predict the Bitcoin TWAP price. 


### Extract-Transform-Load (ETL)

*scripts* contains the source code of the ETL pipeline. Ensure to update the database server name in the db config file [here](/scripts/_config/database.yaml). Upon running the shell script data_prep.sh, the ohlc data will be inserted into the database. Consider this piece as the pre-requisite as until the data collection is done the learning process cannot be started.

Currently, the data is corrected for the period of 6 months (01-Jan-2024 to 30-Sep-2024). Change the start and end date within the script for any preferred date range. Ensure to delete any existing data from the table before running the shell script or else the data will be appended.

### Model Implementation

*predictcrypto* contains the primary source code of the entire model implmentation mechanism. The primary components is "train" while "cmg" is the component manager.

*pipeline* contains the data-pipeline and tranformation-pipeline

*utils* directory comprises of utility functions and methods that is being referred throughout the project.

trainer.sh script is run to train the model and generate the serialized model in a json file which is preferred format for 'prophet'.

### Front-End

Streamlit framework is used for a fast deployment of the front-end web interface. User can provide the inputs, the model is invoked to return the prediction on the web itself.


### Upcoming Changes

1. Support for multiple crypto assets.
2. Tune the model.
3. Schedule the data collection.
4. Verify the prediction w.r.t current price.
5. Integrate MlOps for efficient model registry.
6. If possible migrate the database from local to cloud.

## Support

For any query or discussion, email debmalya.mondal@outlook.com or send me a message on 

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/debmalyamondal)

