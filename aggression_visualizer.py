
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import seaborn as sns

# Load csv file
match_aggr_data = pd.read_csv("soccer_match_aggression_updated.csv", header=0)
team_data = pd.read_csv("european_soccer_dataset-TEAM.csv", header=0)

#print(match_aggr_data['match_api_id'])
#plot_data = sns.load_dataset("soccer_match_aggression_updated")

# Get team to analyze
# Can convert team name to team selection id later
team_selection_name = input("Enter Team Name: ")
team_selection_id = team_data.loc[team_data["team_long_name"] == team_selection_name, "team_api_id"].iloc[0]

print(team_selection_id)

cmap = sns.diverging_palette(30, 250, l=65, s=200, as_cmap=True)
divnorm = mcolors.TwoSlopeNorm(vmin=-8, vcenter=0, vmax=8)

fig, ax = plt.subplots(nrows=1, ncols=2)
fig.tight_layout()

ax[0].set_title("Score Difference of \"" + team_selection_name + "\" Home Games")
ax[1].set_title("Score Difference of \"" + team_selection_name + "\" Away Games")
for ax_i in ax:
    ax_i.set_facecolor((0.9, 0.9, 0.9))
    ax_i.set_xlim([0, 100])
    ax_i.set_ylim([0, 100])
    ax_i.set_xlabel(team_selection_name + " Aggression")
    ax_i.set_ylabel("Opponent Team Aggression")


# Get columns where the team inputted is the home team
match_api_id = match_aggr_data.loc[
    match_aggr_data["home_team_api_id"] == team_selection_id,
    "match_api_id"]
team_goal = match_aggr_data.loc[
    match_aggr_data["home_team_api_id"] == team_selection_id,
    "home_team_goal"]
team_aggression = match_aggr_data.loc[
    match_aggr_data["home_team_api_id"] == team_selection_id,
    "home_team_aggression"]
other_team_goal = match_aggr_data.loc[
    match_aggr_data["home_team_api_id"] == team_selection_id,
    "away_team_goal"]
other_team_aggression = match_aggr_data.loc[
    match_aggr_data["home_team_api_id"] == team_selection_id,
    "away_team_aggression"]
score_diff = match_aggr_data.loc[
    match_aggr_data["home_team_api_id"] == team_selection_id,
    "score_diff"]

# Plot data
ax[0] = ax[0].scatter(team_aggression, other_team_aggression, c=score_diff, cmap=cmap, norm=divnorm)


# Get columns where the team inputted is the away team
match_api_id = match_aggr_data.loc[
    match_aggr_data["away_team_api_id"] == team_selection_id,
    "match_api_id"]
team_goal = match_aggr_data.loc[
    match_aggr_data["away_team_api_id"] == team_selection_id,
    "away_team_goal"]
team_aggression = match_aggr_data.loc[
    match_aggr_data["away_team_api_id"] == team_selection_id,
    "away_team_aggression"]
other_team_goal = match_aggr_data.loc[
    match_aggr_data["away_team_api_id"] == team_selection_id,
    "home_team_goal"]
other_team_aggression = match_aggr_data.loc[
    match_aggr_data["away_team_api_id"] == team_selection_id,
    "home_team_aggression"]
score_diff = match_aggr_data.loc[
    match_aggr_data["away_team_api_id"] == team_selection_id,
    "score_diff"]

# Plot data
ax[1] = ax[1].scatter(team_aggression, other_team_aggression, c=score_diff * -1, cmap=cmap, norm=divnorm)

fig.colorbar(ax[0])
fig.colorbar(ax[1])

plt.show()




