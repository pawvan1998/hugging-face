# main.py

from fetch_models import fetch_top_models, save_report

if __name__ == "__main__":
    report = fetch_top_models()
    save_report(report)
    print("Report generated successfully.")

