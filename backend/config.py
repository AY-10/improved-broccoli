import os
from dotenv import load_dotenv

load_dotenv()

Api_key = os.getenv("Api_key")
Code_runner = os.getenv("Code_runner")

config = {
    'Api_key': Api_key, 'Code_runner': Code_runner
}
