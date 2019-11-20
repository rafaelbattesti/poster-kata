# Requirements and assumptions

## Tools
* Python latest
* Travis CI
* Docker (Docker Compose)
* PostgreSQL latest

## Objectives
* Create a fake customer database: **source**
* Create target database **dw**
* Extract data from **source** and https://swapi.co/
* Merge into **dw**

## Project Setup
- [x] Setup travis
- [x] Setup docker contexts
- [x] Setup docker-compose services

## SWAPI
- [x] Read: https://swapi.co/documentation
- [x] Understand the data available
- [x] Understand the tools

## Database Service
- [x] Home of **source** and **dw** for simplicity
- [x] Create **source**
- [ ] Populate **source**
- [x] Create **dw**

### Source sample data
* poster_content | string | "Millennium Falcon"
* quantity | int | 7
* price | decimal | 2.9
* email | string | "sally_skywalker@gmail.com"
* sales_rep | string | "tej@swposters.com"
* promo_code | string | "radio"

## ETL Service
- [ ] Extraction Layer: API and SQL
- [ ] Transformation Layer: pandas
- [ ] Loading Layer: SQL

## Requirements for dw
- [ ] Populate **source** with what we sell: starship, character, planet
- [ ] Which **films** a **starship** appears and they were **created**
- [ ] Customer email cannot be ingested
- [ ] Data Ingestion should be kept to a minimum
- [ ] User needs to be able to summarize the data