"""Command-line interface."""
import json
from pathlib import Path
from typing import Any, Dict

import click

from moneybird.client import get_client


@click.command()
@click.version_option()
def main() -> None:
    """Moneybird Api Python Client."""

    client = get_client()

    response = client.get("253628522405299379/contacts.json")

    contacts = response.json()

    merged_contact: Dict[str, Any] = {}

    for contact in contacts:
        for key, value in contact.items():
            if key not in merged_contact or not merged_contact[key]:
                merged_contact[key] = value

    json.dump(merged_contact, (Path(__file__).parent / "contacts.json").open("w"))


if __name__ == "__main__":
    main(prog_name="moneybird")  # pragma: no cover
