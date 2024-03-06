# busradar-flensburg

bla weil ichs kann bla


## Prerequisite

Install system dependencies and clone repository

```
sudo apt install git git-lfs virtualenv python3 python3-pip postgresql-16 postgis3
git clone https://github.com/p3t3r67x0/busradar-flensburg.git
```

Insert and run SQL statements. Make sure to replace the values with your own ones

```
sudo -i -Hu postgres psql -U postgres -h localhost -d postgres -p 5434 < busradar-schema.sql
```


Create dot `.env` file inside root directory. Make sure to add the following content repaced by your actual values

```
URL_BASE="https://www.busradar-flensburg.de"
URL_DETAIL="https://www.busradar-flensburg.de/json/busradar/vehiclepos"

DB_PASS=postgres
DB_HOST=localhost
DB_USER=postgres
DB_NAME=postgres
DB_PORT=5432
```

## Setup

Install Postgres and Postgis plugin and python dependencies


## Run

```
uvicorn main:app --reload
```


## Test

```
curl -X 'GET' 'http://127.0.0.1:8000/busradar/v1/details' -H 'accept: application/json'
```
