import json
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("KEY")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {SECRET_KEY}"}

def summerize(text):
    def query(payload):
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))
    data = query(text)
    data2 = data[0]
    data3 = data2.get("summary_text")
    return data3