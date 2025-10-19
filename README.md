# PROG8850 - Assignment 3: NYC 311 Explorer

## Overview
Flask + MySQL project that ingests a slice of NYC 311 Service Requests (January 2023), provides search + aggregate views, and includes Selenium tests.

## Prerequisites
- Docker & docker-compose
- (Local tests) Chrome installed

## Setup & run
1. Ensure `.env` exists (you provided it):
FLASK_ENV=development
FLASK_APP=app/main.py
MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DATABASE=nyc311
APP_PORT=5000

2. Place real January 2023 CSV at: data/311_2023_01.csv
(CI uses `data/sample.csv` automatically.)

3. Start with Docker: docker compose up -d --build

4. Run ETL (populates DB): docker compose exec web python etl/etl.py

5. Open the app: http://localhost:5000


## Tests
- Run locally: pytest -q
