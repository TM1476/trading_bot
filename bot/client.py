from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    return Client(
        os.getenv("UiaGZNhZfv03bxGnjVPjWQZy41nGjjU21ZFodEcdkVeIH2RxKuFajZEnOY3eNdcE"),
        os.getenv("hkqcF71W4Tgy58CwXd6j5Pt20KxC7xk1eXXdhDcJ86zWyMSwrxxXKFmF5myllh1X"),
        testnet=True
    )
