def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    file_secure_protocol = "security_protocols.txt"
    secure_data = None
    file_name = "classified_data.txt"
    file_content = None
    try:
        with open(file_name, 'r') as file_obj:
            file_content = file_obj.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            "ERROR: Storage vault not found. Run data generator first.")
    if file_content:
        print("Initiating secure vault access...\n",
              "Vault connection established with failsafe protocols\n", sep='')
        print("SECURE EXTRACTION:")
        print(file_content)
    try:
        with open(file_secure_protocol, 'r') as f:
            secure_data = f.read()
        with open(file_secure_protocol, 'w') as file:
            file.write(secure_data)
    except FileNotFoundError:
        raise FileNotFoundError(
            "ERROR: Storage vault not found. Run data generator first.")
    if secure_data:
        print("\nSECURE PRESERVATION:")
        print(secure_data)
        print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
