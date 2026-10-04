import requests
import os
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@sabeprono"

def get_pronostics():
    date = datetime.now().strftime("%d/%m/%Y")
    message = f"""
🔥 *SABE PRONO - {date}* 🔥

⚽ Match du jour : Paris SG vs Marseille
💰 Cote : 1.85
🎯 Confiance : 85%
✅ Analyse par Sabe Team

👉 Restez connecté !
"""
    return message

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    r = requests.post(url, data=data)
    print(r.text)

if __name__ == "__main__":
    msg = get_pronostics()
    send_message(msg)
