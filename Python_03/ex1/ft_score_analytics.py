import sys


def ft_handl_scores() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        raise ValueError(
            "No scores provided."
            " Usage: python3 ft_score_analytics.py"
            " <score1> <score2> ...")
    player_scores: list[str] = []
    for arg in sys.argv[1:]:
        try:
            arg: int = int(arg)
        except ValueError:
            raise ValueError(f"Cannot Convert '{arg}' to int()")
        player_scores += [arg]
    print(f"Scores processed: {player_scores}")
    print(f"Total players: {len(player_scores)}")
    print(f"Total score: {sum(player_scores)}")
    print(f"Average score: {sum(player_scores) / len(player_scores):.1f}")
    print(f"High score: {max(player_scores)}")
    print(f"Low score: {min(player_scores)}")
    print(f"Score range: {max(player_scores) - min(player_scores)}")


if __name__ == "__main__":
    try:
        ft_handl_scores()
    except Exception as e:
        print("Error:", e)
