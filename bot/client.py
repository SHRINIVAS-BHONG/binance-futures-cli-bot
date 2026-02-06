import logging
import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise RuntimeError("Missing Binance API credentials")

        self.client = Client(
            api_key=api_key,
            api_secret=api_secret,
            testnet=True
        )

        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logger.info("Binance Futures Testnet client initialized")

    def place_order(self, **kwargs):
        logger.info(f"Placing order: {kwargs}")
        response = self.client.futures_create_order(**kwargs)
        logger.info(f"Order response: {response}")
        return response
