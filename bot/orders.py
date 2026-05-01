from bot.client import get_client
import logging

client = get_client()

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        logging.info(f"MARKET ORDER: {order}")
        return order
    except Exception as e:
        logging.error(f"Market Error: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logging.info(f"LIMIT ORDER: {order}")
        return order
    except Exception as e:
        logging.error(f"Limit Error: {e}")
        raise
