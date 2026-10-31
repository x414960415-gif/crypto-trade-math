"""Calculate a spot trade with percentage fees paid in the quote currency."""

import argparse
from decimal import Decimal, InvalidOperation


def calculate(buy_price, sell_price, quantity, buy_fee, sell_fee):
    values = [Decimal(str(v)) for v in (buy_price, sell_price, quantity, buy_fee, sell_fee)]
    if not all(v.is_finite() for v in values):
        raise ValueError("All values must be finite")
    buy, sell, qty, bf, sf = values
    if buy <= 0 or qty <= 0 or sell < 0 or not 0 <= bf <= 100 or not 0 <= sf < 100:
        raise ValueError("Prices and quantity must be valid; fees must be between 0 and 100%, with sell fee below 100%")
    cost = qty * buy * (1 + bf / 100)
    proceeds = qty * sell * (1 - sf / 100)
    profit = proceeds - cost
    return {"buy_cost": cost, "net_proceeds": proceeds, "net_profit": profit,
            "roi_percent": profit / cost * 100,
            "break_even_sell_price": buy * (1 + bf / 100) / (1 - sf / 100)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("buy-price", "sell-price", "quantity", "buy-fee", "sell-fee"):
        parser.add_argument("--" + name, required=True, type=Decimal)
    args = parser.parse_args()
    try:
        result = calculate(args.buy_price, args.sell_price, args.quantity, args.buy_fee, args.sell_fee)
    except (ValueError, InvalidOperation) as exc:
        parser.error(str(exc))
    for name, value in result.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
