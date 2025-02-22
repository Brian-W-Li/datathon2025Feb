#install.packages("DBI")
#install.packages("RSQLite") 
#install.packages("RMariaDB") 
#install.packages("RPostgres") 
#install.packages("odbc")    

#library(DBI)
#library(RSQLite)

#conn <- dbConnect(RSQLite::SQLite(), "my_database.sqlite")
LEAGUE_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-LEAGUE.csv", 
                        stringsAsFactors = FALSE)
PLAYER_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-PLAYER.csv", stringsAsFactors = FALSE)
PLAYER_ATTRIBUTES_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-PLAYER_ATTRIBUTES.csv", stringsAsFactors = FALSE)
TEAM_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-TEAM.csv", stringsAsFactors = FALSE)
MATCH_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-MATCH.csv", stringsAsFactors = FALSE)
COUNTRY_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-COUNTRY.csv", stringsAsFactors = FALSE)
TEAM_ATTRIBUTES_data <- read.csv("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-TEAM_ATTRIBUTES.csv", stringsAsFactors = FALSE)
#head(LEAGUE_data)
ls()
#head(my_data)
#dbWriteTable(conn, "my_table", my_data, overwrite = TRUE, row.names = FALSE)

#file.exists("/Users/Brian/Downloads/PredictiveModelingTrack-EuropeanSoccerDataset/european_soccer_dataset-LEAGUE.csv")
