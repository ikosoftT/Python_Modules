def track_data() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {'first_kill', 'level_10', 'treasure_hunter',
                       'speed_demon'}
    bob: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie: set[str] = {'level_10', 'treasure_hunter', 'boss_slayer',
                         'speed_demon',
                         'perfectionist'}

    print(f"Player alice achievements: {alice}\n"
          f"Player bob achievements: {bob}\n"
          f"Player charlie achievements: {charlie}\n")
    print("=== Achievement Analytics ===")

    unique_achs: set[str] = alice.union(bob, charlie)

    print(f"All unique achievements: {unique_achs}")
    print(f"Total unique achievements: {len(unique_achs)}\n")
    print("Common to all players: "
          f"{unique_achs.intersection(alice, bob, charlie)}")
    rare_bob: set[str] = bob.difference(alice, charlie)
    rare_charlie: set[str] = charlie.difference(alice, bob)
    rare: set[str] = rare_bob.union(rare_charlie)

    print(f"Rare achievements  (1 player): {rare}\n")

    print(f"Alice vs Bob: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    track_data()
