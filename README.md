# Star Wars Shop Data Warehouse
This is a simple example of a systems that pulls data from different sources and provides visibility to clients

## Development
* Build and run: `docker-compose up --build`
* Destroy: `docker-compose down --volumes`

Tip: when building without destroying the pgdata volume, the whole database initialization is skipped.

## Idea
The idea is to simulate a real data integration project.
In this joly example, we'll be calling it "ProjectSWDemo" - Star Wars Shop Demographics, or "SWS_DEMO"

## Assumptions
A demographics study would require customers' demographic data, such as age, location, etc.
Customer data ingested should be anonymized (PII)

## Components

### Databases

1. **Data Warehouse (Target)**: sws_dw
* **Schemas/Zones**: landing (lz), structured (sz), consumer (cz)

2. **SWS Database (Source)**: sws
* **Schemas**: ordering

### APIs
1. swapi: https://swapi.co/
2. sws_demo_api

## ETL
1. Extraction layer
2. Transformation layer
3. Loading layer

https://www.postgresql.org/docs/9.4/rules-privileges.html
