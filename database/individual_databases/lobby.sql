CREATE TABLE IF NOT EXISTS lobby (
    id INTEGER PRIMARY KEY,
    url TEXT NOT NULL,
    player_name TEXT NOT NULL,
    player_score INTEGER DEFAULT 0
);