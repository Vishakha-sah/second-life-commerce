import json
import os
from typing import List

# File paths for our lightweight local database
PRODUCTS_DB = "products.json"
SELLERS_DB = "sellers.json"
LISTINGS_DB = "listings.json"  # <--- Added for marketplace listings

def initialize_db():
    """Bootstraps the JSON files if they don't exist yet."""
    if not os.path.exists(PRODUCTS_DB):
        with open(PRODUCTS_DB, "w") as f:
            json.dump([], f)

    if not os.path.exists(LISTINGS_DB):
        with open(LISTINGS_DB, "w") as f:
            json.dump([], f)  # <--- Initialize listings as an empty array

    if not os.path.exists(SELLERS_DB):
        with open(SELLERS_DB, "w") as f:
            default_sellers = {
                "user_rahul": {"green_points": 0, "listings_count": 0},
                "user_sakshi": {"green_points": 500, "listings_count": 2}
            }
            json.dump(default_sellers, f, indent=4)

def read_json(file_path: str):
    """Safely reads data from a specified JSON file."""
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return [] if file_path in [PRODUCTS_DB, LISTINGS_DB] else {}

def write_json(file_path: str, data):
    """Safely writes structured data back to the JSON file."""
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# Automatically bootstrap files on import
initialize_db()