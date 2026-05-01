from binance.client import Client
import os

def get_client():
    api_key = os.environ.get("UiaGZNhZfv03bxGnjVPjWQZy41nGjjU21ZFodEcdkVeIH2RxKuFajZEnOY3eNdcE")
    api_secret = os.environ.get("hkqcF71W4Tgy58CwXd6j5Pt20KxC7xk1eXXdhDcJ86zWyMSwrxxXKFmF5myllh1X")

    print("API KEY:", api_key)
    print("SECRET:", api_secret)

    # 👇 DO NOT crash app
    if not api_key or not api_secret:
        print("⚠️ API keys missing → running in DEMO mode")
        return None

    return Client(api_key, api_secret)
    
