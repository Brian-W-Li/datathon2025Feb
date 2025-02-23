
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load csv file
match_aggr_data = pd.read_csv("soccer_match_aggression.csv")

# Get team to analyze
# Can convert team name to team selection id later
team_selection_id = input("Enter Team ID: ")



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




