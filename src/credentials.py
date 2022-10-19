from dataclasses import dataclass
from typing import Iterable
import yaml


@dataclass
class Credentials:
    email: str
    password: str


def get_credentials() -> Iterable[Credentials]:
    with open("./accounts.yml", "r", encoding="utf-8") as f:
        credentials = yaml.full_load(f)
        return map(
            lambda creds: Credentials(email=creds["email"], password=creds["password"]),
            credentials,
        )
