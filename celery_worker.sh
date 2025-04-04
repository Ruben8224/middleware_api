#!/bin/bash
celery -A app.worker.celery worker --loglevel=info