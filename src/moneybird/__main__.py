"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Moneybird Api Python Client."""


if __name__ == "__main__":
    main(prog_name="moneybird-api-python-client")  # pragma: no cover
