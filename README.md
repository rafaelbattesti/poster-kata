<p align="center">
  <img src="https://github.com/rafaelbattesti/poster-kata/blob/master/docs/sw_logo_1.png">
</p>

[![Build Status](https://travis-ci.org/rafaelbattesti/poster-kata.svg?branch=master)](https://travis-ci.org/rafaelbattesti/poster-kata)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# ProjectSWDemo - Star Wars Shop (SWS)
This project implements an ETL service for the fictitious **Star Wars Shop** to extract data from 2 sources namely `swapi` and `sws` db. 

`swapi` is a public service exposing data about Star Wars films, starships and their participation in the films, among other data like characters, planets, etc.

`sws` db is a traditional relational database containing data about the Star Wars Shop `customers`, `products`, `promo codes` and `sales`. The data in `sws` db will be generated by the `svc-datagen` service.

The end goal is to provide an aggregated view of `sales`, `customer demographics` and `product features`.

## Development
* Build and run: `docker-compose up --build`
* Destroy: `docker-compose down --volumes`

Tip: when building without destroying the pgdata volume, the whole database initialization is skipped.

## Assumptions
* A demographics study would require customers' demographic data such as age, location, etc.
* All customer data ingested should be anonymized (GDPR - PII)

## Services

### svc-postgres

1. **Data Warehouse (Target)**: sws_dw
* Schemas/Zones: landing (lz), structured (sz), consumer (cz)

2. **SWS Database (Source)**: sws
* Schemas: ordering

### APIs
1. swapi: https://swapi.co/: to retrieve data from Star Wars films and starships
2. sws_demo_api: Flask API to serve aggregated demographics and sales data (Future implementation)

### svc-datagen
1. Generates data using PyPi Faker.
2. Tables get a configurable rate of NULL fields independently distributed.

### svc-etl
#### 1. Extraction layer
* Extracts data from both sources: `swapi` and `sws` db.
* Dirty load from `csv` into DW landing zone in `TEXT` format.

#### 2. Transformation layer
* Data deduplication from dirty load in the Landing Zone.
* Data cleansing.
* Data casting.

#### 3. Loading Layer
* Populate structured zone tables

## References:
* For table access isolation through views: https://www.postgresql.org/docs/9.4/rules-privileges.html
* For GDPR on PII: https://bostata.com/gdpr-for-engineers-what-is-personal-data/
* For fake data generation: https://faker.readthedocs.io/en/master/
* For DW and DL design: https://static1.squarespace.com/static/52d1b75de4b0ed895b7e7de9/t/59e3bd8464b05fe9e6bbe969/1508097416856/DesigningAModernDWandDataLake_MelissaCoates.pdf