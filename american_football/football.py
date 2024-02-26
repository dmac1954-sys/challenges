def main():

    game_data = [
        {"team": "New England Patriots", "event": "Goal"},
        {"team": "New England Patriots", "event": "Goal"},
        {"team": "New England Patriots", "event": "Goal"},
        {"team": "New England Patriots", "event": "Goal"},
        {"team": "New England Patriots", "event": "Miss"},
        {"team": "New England Patriots", "event": "Miss"},
        {"team": "New York Giants", "event": "Goal"},
        {"team": "New York Giants", "event": "Goal"},
        {"team": "New York Giants", "event": "Goal"},
        {"team": "New York Giants", "event": "Miss"},
        {"team": "New York Giants", "event": "Miss"},
        {"team": "New York Giants", "event": "Miss"},
    ]
    team_name = input("Please enter a team name: ")

    print(calculate_average_goals(team_name, game_data))


def calculate_average_goals(team_name, game_data):
    team_goals = {}
    team_matches = {}
    for entry in game_data:
        if entry["team"] == team_name:
            if entry["team"] not in team_goals:
                team_goals[entry["team"]] = 0
                team_matches[entry["team"]] = 0
            if entry["event"] == "Goal":
                team_goals[entry["team"]] += 1
            team_matches[entry["team"]] += 1

    num_matches = team_matches.get(team_name, 1)
    total_goals = team_goals.get(team_name, 0)

    return total_goals / num_matches

if __name__ == "__main__":
    main()
