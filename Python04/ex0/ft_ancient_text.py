def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ==\n")
    file_name = "ancient_fragment.txt"
    file_object = None

    print(f"Accessing Storage Vault: {file_name}\n")

    try:
        file_object = open(file_name, 'r')
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        if file_object:
            print("Connection established...\n")
            print(f"RECOVERED DATA:\n{file_object.read()}")
    finally:
        if file_object:
            file_object.close()
            print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
