import pandas as pd

match_data = pd.read_csv("/Users/Brian/Downloads/datathon2025_group21/CLEANED1_european_soccer_dataset-MATCH.csv")

playerAttributes_data = pd.read_csv("european_soccer_dataset-PLAYER_ATTRIBUTES.csv")

playerAttributes_data["date"] = pd.to_datetime(playerAttributes_data["date"], errors="coerce") #playerAttributes date are comparable
match_data["date"] = pd.to_datetime(match_data["date"], errors="coerce") #match data date is comparable

#playerAttributes_data["aggression"] = playerAttributes_data["aggression"].fillna(-1) #do i edit this?
#print(playerAttributes_data.sort_values(by = ["aggression"]))
#playerAttributes_data = playerAttributes_data.sort_values(by=["player_id", "date"]).reset_index(drop = True) #sorts playerAttributes_data by player_id first then date

#print(match_data)
home_players = match_data.melt(
    id_vars=["match_api_id", "date"],
    value_vars=[f"home_player_{i}" for i in range(1, 12)],
    var_name="home_position",
    value_name="player_id"
)

away_players = match_data.melt(
    id_vars=["match_api_id", "date"],
    value_vars=[f"away_player_{i}" for i in range(1, 12)],
    var_name="away_position",
    value_name="player_id"
)

# Combine home and away players
all_players = pd.concat([home_players, away_players], ignore_index=True).drop(columns=["home_position", "away_position"])
#del all_players['player_fifa_api_id']
#print(all_players)
all_players.to_csv("CLEANmatchDatePlayers.csv", index=False)

# print(all_players)
# print(playerAttributes_data)

# Step 1: Determine for each player whether they have any valid aggression measurement.
# Group by player_api_id and count non-null aggression values.
# valid_counts = playerAttributes_data.groupby("player_api_id")["aggression"].apply(lambda x: x.notnull().sum()).reset_index(name="valid_count")
# print(valid_counts)

# #Merge the counts back into the attributes DataFrame for ease of filtering.
# df_attributes = playerAttributes_data.merge(valid_counts, on="player_api_id", how="left")
# # print(df_attributes)

# players_all_null = valid_counts[valid_counts["valid_count"] == 0]["player_api_id"]
# # print()
# # print(players_all_null)

# # For these players, remove all rows from df_attributes and also remove them from df_matches.
# df_attributes_clean = df_attributes[~df_attributes["player_api_id"].isin(players_all_null)]
# df_matches_clean = all_players[~all_players["player_id"].isin(players_all_null)]

# # Step 3: For the remaining players (those with at least one valid aggression measurement),
# # drop only the rows where aggression is null.
# df_attributes_clean = df_attributes_clean[df_attributes_clean["aggression"].notnull()]

# # Optionally, if you don't need the 'valid_count' column anymore, drop it.
# df_attributes_clean = df_attributes_clean.drop(columns=["valid_count"])
# print(df_attributes_clean)

# df_attributes_clean.to_csv("player_attributes_clean.csv", index=False)



