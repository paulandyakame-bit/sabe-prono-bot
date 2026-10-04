import requests
import time
from datetime import datetime

# --- CONFIGURATION ---
# Remplace par ton token Telegram (tu me l'enverras après)
TOKEN = "METS_TON_TOKEN_ICI"
CHANNEL_ID = "@sabeprono"  # ou ton ID de canal

def get_pronostics():
    # Ici ton algorithme de pronostics
    # Pour l'instant on envoie un message test
    date = datetime.now().strftime("%d/%m/%Y")
    message = f"""
🔥 *SABE PRONO - {date}* 🔥

⚽ Match du jour : Analyse en cours...
💰 Cote : 1.85
🎯 Confiance : 85%

👉 Reste connecté, les pronos arrivent !
"""
    return message

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)

if __name__ == "__main__":
    print("Bot démarré...")
    prono = get_pronostics()
    send_telegram(prono)
    print("Prono envoyé !")
