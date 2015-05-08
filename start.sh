#!/usr/bin/env bash
cd apps/
source venv/bin/activate
python infopy/manage.py runserver 0.0.0.0:8000
