import requests
import os
import time
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@sabeprono"

def get_pronostics():
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
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
    print("Bot en ligne 24h/24...")
    while True:
        time.sleep(60)
