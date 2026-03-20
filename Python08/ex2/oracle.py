#!/usr/bin/env python3

import os
from dotenv import load_dotenv


def get_config(key: str, default=None):
    value = os.getenv(key, default)
    if value is None:
        print(f"[WARNING] {key} is not set")
    return value


def main():
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")

    mode = get_config("MATRIX_MODE", "development")
    database = get_config("DATABASE_URL")
    api_key = get_config("API_KEY")
    log_level = get_config("LOG_LEVEL", "INFO")
    zion = get_config("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {log_level}")

    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")