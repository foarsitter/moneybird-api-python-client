import os

import httpx

MONEYBIRD_BASE_URL = os.getenv("MONEYBIRD_BASE_URL", "https://moneybird.com/api/v2/")
MONEYBIRD_API_TOKEN = os.getenv("MONEYBIRD_API_TOKEN", "")


def bearer_auth(request: httpx.Request) -> httpx.Request:
    request.headers["Authorization"] = "Bearer " + MONEYBIRD_API_TOKEN
    return request


def get_client() -> httpx.Client:
    httpx_client = httpx.Client(auth=bearer_auth, base_url=MONEYBIRD_BASE_URL)
    return httpx_client
