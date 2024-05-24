# fetch_models.py

import requests
from datetime import datetime

API_URL = "https://huggingface.co/api/models"

def fetch_top_models():
    response = requests.get(API_URL)
    models = response.json()

    top_models = sorted(models, key=lambda x: x['downloads'], reverse=True)[:10]

    report = "Top 10 Hugging Face Models by Downloads:\n"
    report += "Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

    for idx, model in enumerate(top_models):
        report += f"{idx + 1}. {model['modelId']} - Downloads: {model['downloads']}\n"

    return report

def save_report(report, filename="report.txt"):
    with open(filename, "w") as file:
        file.write(report)

