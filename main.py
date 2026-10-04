import requests
import os
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@sabeprono"

def get_pronostics():
    date = datetime.now().strftime("%d/%m/%Y")
    message = f"""
🔥 *SABE PRONO - {date}* 🔥

⚽ Match du jour : Analyse en cours...
💰 Cote : 1.85
🎯 Confiance : 85%

👉 Reste connecté !
"""
    return message

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHANNEL_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, data=data)

if __name__ == "__main__":
    send_telegram(get_pronostics())
