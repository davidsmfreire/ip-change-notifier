import requests
import os
import time
from dotenv import load_dotenv
import logging

def get_public_ipv4():
    url = "https://ipv4.icanhazip.com"
    response = requests.get(url, headers={'Accept': 'text/plain'})

    if response.status_code != 200:
        logging.error("Failed to retrieve your IP address")
        return ""

    return response.text.strip()
    
def send_signal_message(phone_number: str, api_key: str, message: str):
    host = "https://api.callmebot.com"
    endpoint = f"/signal/send.php?phone={phone_number}&apikey={api_key}&text="
    response = requests.get(host + endpoint + message)
    if response.status_code != 200:
        logging.error(f"Bad status code: {response.status_code}")
    logging.info(f"Sending message to {phone_number}: '{message}'")

def main():
    last_ip = os.environ.get("LAST_IP", get_public_ipv4())
    phone_number = os.environ["PHONE_NUMBER"]
    api_key = os.environ["API_KEY"]

    send_signal_message(phone_number, api_key, "Started ip monitor")
    while True:
        time.sleep(300)
        new_ip = get_public_ipv4()
        if new_ip and new_ip != last_ip:
            send_signal_message(phone_number, api_key, f"Public IP changed: {last_ip} -> {new_ip}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    main()
