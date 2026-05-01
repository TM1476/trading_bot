from flask import Flask, request, jsonify, render_template
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_input
from bot.logging_config import setup_logging
import os

app = Flask(__name__)
setup_logging()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/order", methods=["POST"])
def order():
    try:
        data = request.form

        symbol = data.get("symbol")
        side = data.get("side")
        order_type = data.get("type")
        quantity = float(data.get("quantity"))
        price = data.get("price")

        if price:
            price = float(price)

        # Validate input
        validate_input(symbol, side, order_type, quantity, price)

        # Execute order
        if order_type.upper() == "MARKET":
            result = place_market_order(symbol, side, quantity)
        else:
            result = place_limit_order(symbol, side, quantity, price)

        return jsonify({
            "status": "success",
            "data": {
                "orderId": result.get("orderId"),
                "status": result.get("status"),
                "executedQty": result.get("executedQty"),
                "avgPrice": result.get("avgPrice", "N/A")
            }
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


# 🔥 IMPORTANT for deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
