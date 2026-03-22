def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name = "new_discovery.txt"
    file_obj = None
    data = "[ENTRY 001] New quantum algorithm discovered\n" \
        "[ENTRY 002] Efficiency increased by 347%\n" \
        "[ENTRY 003] Archived by Data Archivist trainee\n"

    print(f"Initializing new storage unit: {file_name}")
    file_obj = open(file_name, 'w')
    if file_obj:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        file_obj.write(data)
        print(data)
        file_obj.close()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
