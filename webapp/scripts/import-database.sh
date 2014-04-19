#!/bin/bash
cd /opt/dispatch
python manage.py loaddata fixtures/database.json
