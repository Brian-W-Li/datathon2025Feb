import pandas as pd

match_data = pd.read_csv("/Users/Brian/Downloads/datathon2025_group21/CLEANED1_european_soccer_dataset-MATCH.csv")

playerAttributes_data = pd.read_csv("european_soccer_dataset-PLAYER_ATTRIBUTES.csv")

playerAttributes_data["date"] = pd.to_datetime(playerAttributes_data["date"], errors="coerce") #playerAttributes date are comparable
match_data["date"] = pd.to_datetime(match_data["date"], errors="coerce") #match data date is comparable

playerAttributes_data = playerAttributes_data.rename(columns={"player_api_id": "player_id"}) #renamed column of playerAttributes_data to player_id
#playerAttributes_data["aggression"] = playerAttributes_data["aggression"].fillna(-1) #do i edit this?
print(playerAttributes_data.sort_values(by = ["aggression"]))
playerAttributes_data = playerAttributes_data.sort_values(by=["player_id", "date"]).reset_index(drop = True) #sorts playerAttributes_data by player_id first then date

print(match_data)
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
print(all_players.sort_values(by = ["player_id"]))

# # Fill missing player IDs with -1 and convert to integer
# all_players["player_id"] = all_players["player_id"].fillna(-1).astype(int) #do i change this?

# # Ensure all dates are in datetime64 format
# all_players["date"] = pd.to_datetime(all_players["date"], errors="coerce")

# # Sort all_players before merge_asof
# all_players = all_players.sort_values(by=["player_id", "date"]).reset_index(drop=True)
# print("all_players\n")
# print(all_players)

# print("playerAttributes_data\n")
# print(playerAttributes_data)




# players_df = pd.merge_asof(
#     all_players,
#     playerAttributes_data,
#     by="player_id",
#     left_on="date",
#     right_on="date",
#     direction="backward"
# )
# print(players_df)

# playerAttributes_data.sort_values(by = ["date"], inplace = True)
# match_data.sort_values(by = ["date"], inplace = True)

# home_players = match_data.melt(
#     id_vars=["match_api_id", "date"],  # Columns to keep
#     value_vars=[f"home_player_{i}" for i in range(1, 12)],  # Columns to convert
#     var_name="home_position",  # New column name for original column names
#     value_name="player_id"  # New column name for values (player IDs)
# )

# #print(home_players)

# away_players = match_data.melt(
#     id_vars=["match_api_id", "date"],
#     value_vars=[f"away_player_{i}" for i in range(1, 12)],
#     var_name="away_position",
#     value_name="player_id"
# )

# # print()
# # print(away_players)

# #now if you put these two charts together you get a more accessible chart
# all_players = pd.concat([home_players, away_players], ignore_index=True)
# all_players = all_players.drop(columns = ["home_position"])
# all_players = all_players.drop(columns = ["away_position"])
# #all_players["date"] = pd.to_datetime(all_players["date"], errors="coerce")
# all_players["player_id"] = all_players["player_id"].fillna(-1).astype(int)
# all_players = all_players.sort_values(by=["player_id", "date"]).reset_index(drop=True)
# #print(all_players)#all players is an array with all matches the date of the match and the player_id

# playerAttributes_data = playerAttributes_data.rename(columns={"player_api_id": "player_id"})
# #playerAttributes_data = playerAttributes_data.sort_values(by = ["player_id"]) #there are no null player_id's
# #playerAttributes_data = playerAttributes_data.sort_values(by = ["aggression"]) #there are null aggression values
# playerAttributes_data["aggression"] = playerAttributes_data["aggression"].fillna(-1)


# # print(playerAttributes_data)
# # print(all_players)
# players_df = pd.merge_asof(
#     all_players,
#     playerAttributes_data.sort_values(by=["player_id", "date"]),
#     by="player_id",
#     left_on="date",
#     right_on="date",
#     direction="backward"
# )

# print(players_df)

# #now, combine with player_attributes sorted by date also to find the closest aggression measurement to that date

# # playerAttributes_data = playerAttributes_data.drop(columns = ["player_fifa_api_id"])
# # playerAttributes_data = playerAttributes_data.reset_index(drop = True)
# # print(playerAttributes_data)


