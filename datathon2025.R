#install.packages("DBI")
#install.packages("RSQLite") 
#install.packages("RMariaDB") 
#install.packages("RPostgres") 
#install.packages("odbc")    

#library(DBI)
#library(RSQLite)

conn <- dbConnect(RSQLite::SQLite(), "my_database.sqlite")
LEAGUE_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-LEAGUE.csv", 
                        stringsAsFactors = FALSE)
PLAYER_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-PLAYER.csv", stringsAsFactors = FALSE)
PLAYER_ATTRIBUTES_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-PLAYER_ATTRIBUTES.csv", stringsAsFactors = FALSE)
TEAM_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-TEAM.csv", stringsAsFactors = FALSE)
MATCH_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-MATCH.csv", stringsAsFactors = FALSE)
COUNTRY_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-COUNTRY.csv", stringsAsFactors = FALSE)
TEAM_ATTRIBUTES_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-TEAM_ATTRIBUTES.csv", stringsAsFactors = FALSE)
#head(LEAGUE_data)
# Write each data frame to the SQLite database
dbWriteTable(conn, "LEAGUE", LEAGUE_data, overwrite = TRUE, row.names = FALSE)
dbWriteTable(conn, "PLAYER", PLAYER_data, overwrite = TRUE, row.names = FALSE)
dbWriteTable(conn, "PLAYER_ATTRIBUTES", PLAYER_ATTRIBUTES_data, overwrite = TRUE, row.names = FALSE)
dbWriteTable(conn, "TEAM", TEAM_data, overwrite = TRUE, row.names = FALSE)
dbWriteTable(conn, "MATCH", MATCH_data, overwrite = TRUE, row.names = FALSE)
dbWriteTable(conn, "COUNTRY", COUNTRY_data, overwrite = TRUE, row.names = FALSE)
dbWriteTable(conn, "TEAM_ATTRIBUTES", TEAM_ATTRIBUTES_data, overwrite = TRUE, row.names = FALSE)
dbListTables(conn)
head(MATCH_data)

#query <- "SELECT p.player_name, pa.aggression
          #FROM PLAYER_ATTRIBUTES pa
          #JOIN PLAYER p ON p.player_api_id = pa.player_api_id
          #ORDER BY pa.aggression DESC
          #LIMIT 11;"

#aggressive_players <- dbGetQuery(conn, query)
#print(aggressive_players)
query <- "WITH AggressionByTeam AS {
  SELECT MATCH.home_team_api_id
}"



#head(my_data)
#dbWriteTable(conn, "my_table", my_data, overwrite = TRUE, row.names = FALSE)

