def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    Players_data: list[dict[str, str | int | bool]] = [
        {"name": "yassine", "score": 2650, "status": True, "region": "south"},
        {"name": "Osama", "score": 3650, "status": True, "region": "central"},
        {"name": "Hamid", "score": 1650, "status": False, "region": "east"},
    ]

    print("=== List Comprehension Examples ===")

    High_scores: list[str] = [
        p['name'] for p in Players_data if p['score'] > 2000]

    scores_doubled: list[int] = [
        p['score'] * 2 for p in Players_data]

    Active_players: list[str] = [
        p['name'] for p in Players_data if p['status'] is True]

    print(f"High Scorers (> 2000): {High_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {Active_players}")

    print("\n=== Dict Comprehension Examples ===")
    print("Player scores:", end=' ')

    player_scores: dict[str, int] = {
        p['name']: p['score'] for p in Players_data
    }

    print(player_scores)

    score_category: dict[str, int] = {
        "high": len([p for p in Players_data if p['score'] >= 3000]),
        "Mid": len([p for p in Players_data if 2000 <= p['score'] <= 3000]),
        "low": len([p for p in Players_data if p['score'] < 2000])
    }

    print(f"Score categories: {score_category}")

    player_achivs: dict[str, list[str]] = {
        "yassine": ['first_kill', 'level_10', 'boss_slayer'],
        "Osama": ['first_kill', 'level_10', 'boss_slayer',
                  "perfecto", 'Winner'],
        "hamid": ['first_kill', 'level_10', 'boss_slayer', 'perfecto',
                  'Winner', 'TopG']
    }

    achive_count: dict[str, int] = {
        name: len(achivs)
        for name, achivs in player_achivs.items()
    }

    print(f"Achievement counts: {achive_count}")

    print("\n=== Set Comprehension Examples ===")

    unique_players: set[str] = {p['name'] for p in Players_data}

    Unique_achivs: set[str] = {
        ach
        for ach_list in player_achivs.values()
        for ach in ach_list
    }

    active_regions: set[str] = {
        reg['region']
        for reg in Players_data
        if reg['status'] is True
    }

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {Unique_achivs}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total Players: {len(Players_data)}")
    print(f"Total unique achievements: {len(Unique_achivs)}")

    avg: float = sum(p for p in player_scores.values()) / len(Players_data)

    print(f"Average score: {avg:.1f}")

    scores: list[int] = [p['score'] for p in Players_data]
    max_score: int = max(scores)

    top_player: list[dict[str, str | int | bool]] = [
        p for p in Players_data if p['score'] == max_score
    ]

    print(f"Top performer: {top_player[0]['name']}",
          f"({top_player[0]['score']} points,",
          f"{len(player_achivs[top_player[0]['name']])} achievements)")


if __name__ == "__main__":
    main()
