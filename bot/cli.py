import argparse
import logging
from binance.exceptions import BinanceAPIException

from bot.logging_config import setup_logging
from bot.validators import validate_inputs
from bot.client import BinanceClient
from bot.orders import place_market_order, place_limit_order


def print_order_summary(args):
    print("\n📌 Order Request Summary")
    print("------------------------")
    print(f"Symbol     : {args.symbol}")
    print(f"Side       : {args.side}")
    print(f"Order Type : {args.type}")
    print(f"Quantity   : {args.quantity}")
    if args.type == "LIMIT":
        print(f"Price      : {args.price}")


def print_success_response(response):
    print("\n✅ Order placed successfully")
    print("-----------------------------")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")


def main():
    # Setup logging (file-only, no console noise)
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Step 1: Validate input
        validate_inputs(args)

        # Step 2: Print order request summary
        print_order_summary(args)

        # Step 3: Initialize Binance client
        client = BinanceClient()

        # Step 4: Place order
        if args.type == "MARKET":
            response = place_market_order(
                client,
                args.symbol,
                args.side,
                args.quantity
            )
        else:
            response = place_limit_order(
                client,
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        # Step 5: Print success response
        print_success_response(response)

    except BinanceAPIException as e:
        logger.exception("Binance API rejected the order")
        print("\n❌ Order rejected by Binance Exchange")
        print("-----------------------------------")
        print(e.message)

    except ValueError as e:
        logger.warning(f"Validation error: {e}")
        print("\n❌ Invalid input")
        print("----------------")
        print(e)

    except Exception:
        logger.exception("Unexpected application error")
        print("\n❌ Unexpected error occurred. Check logs for details.")


if __name__ == "__main__":
    main()
