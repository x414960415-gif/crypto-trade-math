# Crypto Trade Math

A small, dependency-free Python utility for calculating the result of a spot crypto trade with separate buy and sell fees. It uses decimal arithmetic and runs locally.

## Usage

```sh
python trade.py --buy-price 100 --sell-price 120 --quantity 2 --buy-fee 0.5 --sell-fee 0.5
```

Fee arguments are percentages: `0.5` means 0.5%. Results are printed in the same quote currency as the input prices. This models fees paid in the quote currency; it does not cover taxes, network fees, slippage, or fees paid in another asset.

For a browser-based calculator and a downloadable trade worksheet, visit [Coin Break Even](https://coinbreakeven.com/).

## Calculations

- Buy cost = quantity × buy price × (1 + buy fee rate)
- Net proceeds = quantity × sell price × (1 − sell fee rate)
- Net profit = net proceeds − buy cost
- Return on investment = net profit / buy cost × 100
- Break-even sell price = buy price × (1 + buy fee rate) / (1 − sell fee rate)

Inputs are hypothetical trade values; this tool does not provide live prices or investment advice.
