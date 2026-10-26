
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from epita_sarang_radha_krishnapillai_crypto.client import get_prices

console = Console()


def main():
    try:
        response = get_prices()
        display = response["DISPLAY"]

        table = Table(title="Live Cryptocurrency Prices")
        table.add_column("Cryptocurrency", style="cyan")
        table.add_column("Currency", style="green")
        table.add_column("Price", style="magenta")

        for symbol in ("BTC", "ETH"):
            for currency in ("USD", "EUR"):
                price = display[symbol][currency]["PRICE"]
                table.add_row(symbol, currency, price)

        console.print(
            Panel(
                table,
                title="EPITA Engineering Tools — TP2",
                expand=False,
            )
        )

    except Exception as error:
        console.print(f"[bold red]Execution Error:[/bold red] {error}")


if __name__ == "__main__":
    main()
