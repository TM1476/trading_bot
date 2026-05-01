from flask import Flask, request, jsonify, render_template
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

app = Flask(__name__)
setup_logging()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/order", methods=["POST"])
def order():
    data = request.form

    symbol = data.get("symbol")
    side = data.get("side")
    order_type = data.get("type")
    quantity = float(data.get("quantity"))
    price = data.get("price")

    if price:
        price = float(price)

    try:
        validate_input(symbol, side, order_type, quantity, price)

        if order_type == "MARKET":
            result = place_market_order(symbol, side, quantity)
        else:
            result = place_limit_order(symbol, side, quantity, price)

        return jsonify({"status": "success", "data": result})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
