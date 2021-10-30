CREATE TABLE IF NOT EXISTS url
(
    id  INTEGER PRIMARY KEY,
    url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS lobby
(
    id           INTEGER PRIMARY KEY,
    url          TEXT NOT NULL,
    player_name  TEXT NOT NULL,
    player_score INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS dictionary
(
    id         INTEGER PRIMARY KEY,
    url        TEXT NOT NULL,
    word       TEXT NOT NULL,
    definition TEXT NOT NULL
);