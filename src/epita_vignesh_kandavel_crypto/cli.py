from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .client import fetch_live_data

console = Console()


def main():
    """Display live cryptocurrency prices in the terminal."""
    try:
        data = fetch_live_data()

        table = Table(title="Live Cryptocurrency Prices")
        table.add_column("Cryptocurrency", style="cyan")
        table.add_column("Currency", style="magenta")
        table.add_column("Price", justify="right", style="green")
        table.add_column("Market Cap", justify="right")

        for symbol in ("BTC", "ETH"):
            for currency in ("USD", "EUR"):
                price = data.get(f"{symbol}_{currency}_price")
                market_cap = data.get(f"{symbol}_{currency}_market_cap")

                if price is not None:
                    table.add_row(
                        symbol,
                        currency,
                        f"{price:,.2f}",
                        f"{market_cap:,.2f}" if market_cap is not None else "N/A",
                    )

        console.print(
            Panel("Data retrieved successfully from CryptoCompare",
                  title=data.get("status", "API Status"))
        )
        console.print(table)

    except Exception as error:
        console.print(f"[bold red]Error:[/bold red] {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()