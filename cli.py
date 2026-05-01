import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--qty", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_input(args.symbol, args.side, args.type, args.qty, args.price)

    if args.type.upper() == "MARKET":
        order = place_market_order(args.symbol, args.side, args.qty)
    else:
        order = place_limit_order(args.symbol, args.side, args.qty, args.price)

    print("✅ Order Success:", order)

except Exception as e:
    print("❌ Error:", e)
