# busradar-flensburg

bla weil ichs kann bla


## Prerequisite

Install system dependencies and clone repository

```
sudo apt install git git-lfs python3 python3-pip python3-venv postgresql-16 postgis3
git clone https://github.com/p3t3r67x0/busradar-flensburg.git
cd busradar-flensburg
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```


## Database

Insert and run SQL statements. Make sure to replace the values with your own ones

```
sudo -i -Hu postgres psql -U postgres -h localhost -d postgres -p 5434 < busradar-schema.sql
```


## Enviroment

Create dot `.env` file inside root directory. Make sure to add the following content repaced by your actual values

```
LINE_1="#00b458"
LINE_2="#f2ee00"
LINE_3="#97dc4d"
LINE_4="#fe9ec9"
LINE_5A="#f40033"
LINE_5B="#f40033"
LINE_7="#7183c2"
LINE_8A="#f49f25"
LINE_8B="#f49f25"
LINE_10="#87d7f5"
LINE_11="#af1a82"
LINE_12="#40f7bd"
LINE_14="#ad8f70"

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


## Development

```
uvicorn main:app --reload
```

## Service

```
[Unit]
Description=API instance for Busradar Flensburg
After=network.target
Requires=postgresql.service

[Service]
Type=simple
User=c3fl
Group=c3fl
DynamicUser=true

WorkingDirectory=/home/c3fl/busrader-flensburg
PrivateTmp=true

EnvironmentFile=/home/c3fl/busrader-flensburg/.env
ExecStart=/home/c3fl/busrader-flensburg/venv/bin/uvicorn \
        --proxy-headers \
        --forwarded-allow-ips='*' \
        --workers=4 \
        --port=8000 \
        main:app

ExecReload=/bin/kill -HUP ${MAINPID}
RestartSec=1
Restart=always

[Install]
WantedBy=multi-user.target
```


## Test

```
curl -X 'GET' 'http://127.0.0.1:8000/busradar/v1/details' -H 'accept: application/json'
```
