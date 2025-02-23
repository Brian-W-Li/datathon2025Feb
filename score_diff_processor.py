import pandas as pd

#data = pd.read_csv("soccer_match_aggression.csv")
data = pd.read_csv("fake_data.csv")

data["score_diff"] = data["home_team_goal"] - data["away_team_goal"]

data.to_csv("soccer_match_aggression_updated.csv")

