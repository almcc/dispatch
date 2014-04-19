#!/bin/bash
cd /opt/dispatch
mkdir -p /opt/dispatch/fixtures
python manage.py dumpdata --format=json --exclude=contenttypes --exclude=auth --exclude=sessions --exclude=sites --exclude=admin  > /opt/dispatch/fixtures/database-ugliy.json
python -mjson.tool /opt/dispatch/fixtures/database-ugliy.json > /opt/dispatch/fixtures/database.json
rm /opt/dispatch/fixtures/database-ugliy.json
