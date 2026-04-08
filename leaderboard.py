import json

def load_leaderboard():
    try:
        with open("scores.json", "r") as file:
            data = json.load(file)
        return data["leaderboard"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return []

def save_score(initials, score):
    leaderboard = load_leaderboard()
    entry = {
        "initials": initials,
        "score": score,
    }
    leaderboard.append(entry)
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
    sliced_leaderboard = sorted_leaderboard[:10]
    data = {"leaderboard": sliced_leaderboard}

    with open("scores.json", "w") as file:
        json.dump(data, file, indent=4)