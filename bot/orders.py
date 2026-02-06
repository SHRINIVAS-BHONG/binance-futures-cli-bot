import logging
from .client import BinanceClient

logger = logging.getLogger(__name__)

def place_market_order(client, symbol, side, quantity):
    return client.place_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

def place_limit_order(client, symbol, side, quantity, price):
    return client.place_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        timeInForce="GTC",
        quantity=quantity,
        price=price
    )
