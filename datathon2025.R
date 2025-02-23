#install.packages("DBI")
library(DBI)
library(RSQLite)
library(lubridate)
library(dplyr)

PLAYER_ATTRIBUTES_data <- read.csv("/Users/Brian/Downloads/datathon2025_group21/european_soccer_dataset-PLAYER_ATTRIBUTES.csv", 
                                   stringsAsFactors = FALSE)
MATCH_data <- read.csv("/Users/Brian/Downloads/datathon2025_group21/european_soccer_dataset-MATCH.csv", 
                       stringsAsFactors = FALSE)
TEAM_data <- read.csv("/Users/Brian/Downloads/datathon2025_group21/european_soccer_dataset-TEAM.csv", 
                      stringsAsFactors = FALSE)

#fixes dates in csv file to comparable dates
PLAYER_ATTRIBUTES_data$date <- as.character(as.Date(parse_date_time(PLAYER_ATTRIBUTES_data$date, orders = c("Y/m/d H:M"))))
MATCH_data$date <- as.character(as.Date(parse_date_time(MATCH_data$date, orders = c("m/d/y H:M"))))

#todo: still need to deal with null values in MATCH.data
#connect to sqllite

conn <- dbConnect(SQLite(), "soccer_data.sqlite")

dbWriteTable(conn, "PLAYER_ATTRIBUTES", PLAYER_ATTRIBUTES_data, overwrite = TRUE, row.names = FALSE)
dbWriteTable(conn, "MATCH", MATCH_data, overwrite = TRUE, row.names = FALSE)
dbWriteTable(conn, "TEAM", TEAM_data, overwrite = TRUE, row.names = FALSE)

#this creates a temp table with the greatest aggression value for each player
#as well as their date of measurement
#dbExecute(conn, "
    #CREATE TEMP TABLE LATEST_PLAYER_AGGRESSION AS
    #SELECT player_api_id, aggression, date
    #FROM PLAYER_ATTRIBUTES
    #WHERE (player_api_id, date) IN (
        #SELECT player_api_id, MAX(date)
        #FROM PLAYER_ATTRIBUTES
        #GROUP BY player_api_id
    #);
#")
dbExecute(conn, "CREATE TEMP TABLE MOST_RECENT_AGGRESSION AS
SELECT pa.player_api_id, pa.aggression, pa.date, m.match_api_id, m.date AS match_date
FROM PLAYER_ATTRIBUTES pa
JOIN MATCH m
ON pa.player_api_id IN (
    COALESCE(m.home_player_1, -1), COALESCE(m.home_player_2, -1), COALESCE(m.home_player_3, -1),
    COALESCE(m.home_player_4, -1), COALESCE(m.home_player_5, -1), COALESCE(m.home_player_6, -1),
    COALESCE(m.home_player_7, -1), COALESCE(m.home_player_8, -1), COALESCE(m.home_player_9, -1),
    COALESCE(m.home_player_10, -1), COALESCE(m.home_player_11, -1),
    COALESCE(m.away_player_1, -1), COALESCE(m.away_player_2, -1), COALESCE(m.away_player_3, -1),
    COALESCE(m.away_player_4, -1), COALESCE(m.away_player_5, -1), COALESCE(m.away_player_6, -1),
    COALESCE(m.away_player_7, -1), COALESCE(m.away_player_8, -1), COALESCE(m.away_player_9, -1),
    COALESCE(m.away_player_10, -1), COALESCE(m.away_player_11, -1)
)
WHERE pa.date <= m.date
AND pa.date = (
    SELECT MAX(pa2.date)
    FROM PLAYER_ATTRIBUTES pa2
    WHERE pa2.player_api_id = pa.player_api_id
    AND pa2.date <= m.date
);")

dbExecute(conn, "")

dbExecute(conn, "
    CREATE TEMP TABLE MOST_RECENT_AGGRESSION AS
    SELECT lpa.player_api_id, lpa.aggression, lpa.date, m.match_api_id
    FROM LATEST_PLAYER_AGGRESSION lpa
    JOIN MATCH m
    ON lpa.date <= m.date;
")
#this creates a table where 

#result <- dbGetQuery(conn, "SELECT * FROM LATEST_PLAYER_AGGRESSION")
#print(result)

#result1 <- dbGetQuery(conn, "SELECT * FROM MOST_RECENT_AGGRESSION")
#print(result1[10000:10050, ])
dbExecute(conn, "CREATE INDEX IF NOT EXISTS idx_mra_player ON MOST_RECENT_AGGRESSION (player_api_id, match_api_id);")
dbExecute(conn, "CREATE INDEX IF NOT EXISTS idx_match_home ON MATCH (match_api_id, home_team_api_id, away_team_api_id);")

dbExecute(conn, "
    CREATE TEMP TABLE HOME_TEAM_AGGRESSION AS
    SELECT m.match_api_id, m.home_team_api_id, AVG(mra.aggression) AS home_team_aggression
    FROM MATCH m
    JOIN MOST_RECENT_AGGRESSION mra
    ON mra.player_api_id IN (
        m.home_player_1, m.home_player_2, m.home_player_3, m.home_player_4,
        m.home_player_5, m.home_player_6, m.home_player_7, m.home_player_8,
        m.home_player_9, m.home_player_10, m.home_player_11
    ) AND mra.match_api_id = m.match_api_id
    GROUP BY m.match_api_id, m.home_team_api_id;
")

result2 <- dbGetQuery(conn, "SELECT * FROM HOME_TEAM_AGGRESSION LIMIT 1000")
print(result2);





