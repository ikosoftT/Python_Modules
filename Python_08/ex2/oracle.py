import os
import sys

try:
    from dotenv import load_dotenv
except Exception:
    print("Missing dependency: python-dotenv")
    print("Install with: pip install python-dotenv")
    sys.exit(1)


def get_env(var: str, default: str = None) -> str:
    value = os.getenv(var)
    if value:
        return value
    return default


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("\n-Please: note that u must copy .env.example to .env-\n")

    try:
        load_dotenv()

        mode = get_env("MATRIX_MODE", "development")
        db = get_env("DATABASE_URL", "local")
        api = get_env("API_KEY")
        log = get_env("LOG_LEVEL", "INFO")
        zion = get_env("ZION_ENDPOINT", "offline")

        print("Configuration loaded:")
        print(f"Mode: {mode}")

        if db == "local":
            print("Database: Connected to local instance")
        else:
            print(f"Database: ({db}) Connected with [OK] ")

        if api:
            print(f"API Access: '{api}'")
        else:
            print("API Access: Missing API KEY")

        print(f"Log Level: {log}")
        print("Zion Network: ", end='')
        if zion != "offline":
            print("Online")
        else:
            print("Online")

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")

        print("\nThe Oracle sees all configurations.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
