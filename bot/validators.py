def validate_input(symbol, side, order_type, quantity, price):
    if not symbol:
        raise ValueError("Symbol required")

    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Invalid side")

    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid type")

    if quantity <= 0:
        raise ValueError("Invalid quantity")

    if order_type.upper() == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT")
