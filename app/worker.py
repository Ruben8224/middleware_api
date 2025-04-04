from celery import Celery

celery = Celery("middleware", config_source="celeryconfig")
