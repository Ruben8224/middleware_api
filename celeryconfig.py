import os
from dotenv import load_dotenv

load_dotenv()

broker_url = os.getenv("REDIS_URL")
result_backend = os.getenv("REDIS_URL")

task_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'

# Aiven usa rediss:// (SSL), se requiere esta config
broker_use_ssl = {
    "ssl_cert_reqs": "none"
}
result_backend_use_ssl = {
    "ssl_cert_reqs": "none"
}
