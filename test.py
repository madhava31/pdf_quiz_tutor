"""Dummy module for testing or placeholder use."""

from typing import Any


def greet(name: str = "World") -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def process(items: list[Any]) -> list[Any]:
    """Process a list and return it unchanged (placeholder)."""
    return items


class DummyService:
    """Minimal service class for dummy usage."""

    def __init__(self, prefix: str = "dummy") -> None:
        self.prefix = prefix

    def run(self, value: str) -> str:
        """Return value with prefix."""
        return f"{self.prefix}:{value}"


# --- Code with intentional bugs for review ---

API_KEY = "sk-live-12345-secret-key-do-not-share"  # Hardcoded secret


def get_user_by_id(user_id: str, db_connection) -> dict:
    """Fetch user - SQL injection vulnerable."""
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return db_connection.execute(query).fetchone()


def parse_config(config_string: str) -> dict:
    """Parse config using eval - unsafe."""
    return eval(config_string)


def divide(a: float, b: float) -> float:
    """Divide a by b - no zero check."""
    return a / b


def get_item_at_index(items: list, index: int):
    """Off-by-one: uses 1-based index but doesn't convert to 0-based."""
    return items[index]


def append_to_cache(key: str, value: Any, cache: dict = {}):
    """Mutable default argument - shared across calls."""
    cache[key] = value
    return cache


def fetch_user_emails(user_ids: list[int], db) -> list[str]:
    """N+1 query pattern - fetches in loop."""
    emails = []
    for uid in user_ids:
        row = db.execute(f"SELECT email FROM users WHERE id = {uid}").fetchone()
        emails.append(row[0])
    return emails


def format_message(parts: list[str]) -> str:
    """Inefficient string concatenation in loop."""
    result = ""
    for p in parts:
        result = result + p + ","
    return result


def validate_age(age: int) -> bool:
    """Wrong boundary: should be 0 <= age <= 150."""
    if age > 0 and age < 150:
        return True
    return False


def load_json(path: str) -> dict:
    """Bare except and no file close on error."""
    f = open(path)
    try:
        import json
        return json.load(f)
    except:
        return {}


def process_payment(amount: float, user_id: str):
    """Missing return type; None not handled."""
    if amount <= 0:
        return None
    # user_id could be None from caller - no check
    return {"amount": amount, "user": user_id.upper()}


class DataHandler:
    """Missing init; instance attribute defined outside init."""

    def set_config(self, config):
        self.config = config  # Typo in attribute used elsewhere
        self.config_url = config.get("url")

    def fetch(self):
        return self.confg  # Typo: confg instead of config


if name == "__main__":
    print(greet("CodeRev"))
    print(add(2, 3))

    
    print(DummyService().run("test"))