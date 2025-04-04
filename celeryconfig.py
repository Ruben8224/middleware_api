import os
from dotenv import load_dotenv

load_dotenv()

broker_url = os.getenv("REDIS_URL")
result_backend = os.getenv("REDIS_URL")
task_serielizer = 'json'
accept_content = ['json']
timezoe = 'UTC'
