# Assign scores to individuals

def assign_individual_score(data, individual_name, score):
    if individual_name not in data["individuals"]:
        return f"Individual {individual_name} not found!"
    if not (0 <= score <= 100):
        return "Score must be between 0 and 100!"
    data["scores"]["individual_scores"][individual_name] = score
    return f"Score of {score} assigned to {individual_name} successfully!"

# Assign scores to team members

def assign_team_member_score(data, team_name, member_name, score):
    if team_name not in data["teams"]:
        return f"Team {team_name} not found!"
    if member_name not in data["teams"][team_name]:
        return f"Member {member_name} not found in Team {team_name}!"
    if not (0 <= score <= 100):
        return "Score must be between 0 and 100!"
    data["scores"]["team_scores"].setdefault(team_name, {})[member_name] = score
    return f"Score of {score} assigned to {member_name} in Team {team_name} successfully!"

# Update leaderboard display to be more user-friendly
def calculate_team_scores(data):
    team_totals = {}
    for team_name, members in data["teams"].items():
        scores = [data["scores"]["team_scores"].get(team_name, {}).get(member, 0) for member in members]
        if scores:
            team_totals[team_name] = {
                "average_score": sum(scores) / len(scores),
                "members": {member: data["scores"]["team_scores"].get(team_name, {}).get(member, 0) for member in members}
            }
        else:
            team_totals[team_name] = {"average_score": 0, "members": {}}
    return team_totals

# Update determine_winners to use the new team score calculation
def determine_winners(data):
    # Individual winner
    individual_scores = data["scores"]["individual_scores"]
    individual_winner = max(individual_scores, key=individual_scores.get, default=None)

    # Team winner
    team_totals = calculate_team_scores(data)
    team_winner = max(team_totals, key=lambda t: team_totals[t]["average_score"], default=None)

    return {
        "individual_winner": individual_winner,
        "team_winner": team_winner,
        "individual_scores": individual_scores,
        "team_totals": team_totals
    }

# Update export_results to use a default file name
from tkinter import filedialog

def export_results(data, file_path=None):
    if not file_path:
        file_path = filedialog.asksaveasfilename(
            initialfile="EventWiz-results.txt",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if not file_path:
            return "Export cancelled."

    results = determine_winners(data)
    with open(file_path, "w") as f:
        f.write("Individual Scores:\n")
        for individual, score in results["individual_scores"].items():
            f.write(f"{individual}: {score}\n")

        f.write("\nTeam Scores:\n")
        for team, total in results["team_totals"].items():
            f.write(f"{team}: {total['average_score']}\n")
            for member, score in total["members"].items():
                f.write(f"  {member}: {score}\n")

        f.write("\nWinners:\n")
        f.write(f"Individual Winner: {results['individual_winner']}\n")
        f.write(f"Team Winner: {results['team_winner']}\n")

    return f"Results exported to {file_path} successfully!"