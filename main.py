import os
import requests

# Retrieve credentials from GitHub Secrets
BOT_TOKEN = os.getenv("8767695621:AAFv11-DCnAGcJ2oTIWUlT20XBdTpJsBCQs")
CHANNEL_ID = os.getenv("@tgminiappsupdates")


def send_hourly_message():
    # Buying Old Tinder Accounts 🔥

2010 – 2024 (All Months) = 22 USDT
2025 first 5 months 17
All age accepted
2025 also 1-5 months

We need old tinder account 
2025 7-12 girl account @Kreegyr

I ALSO NEED ASHLEY MADISON FEMALE ACCOUNTS
    message = "⏰ **Hourly Update**\n\nThis is an automated hourly post for the channel!"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown",  # Allows basic formatting like bold/italics
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Successfully posted to Telegram!")
    else:
        print(f"Failed to post: {response.text}")


if __name__ == "__main__":
    send_hourly_message()
