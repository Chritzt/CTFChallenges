
DROP TABLE IF EXISTS CoffeeBot;

CREATE TABLE CoffeeBot (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            description TEXT NOT NULL
);

CREATE TABLE Secret (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           description TEXT NOT NULL
);

INSERT INTO CoffeeBot (name, description) VALUES
('Coffee', 'Classic Coffee'),
('Tee', 'To Calm you down');

INSERT INTO Secret (name, description) VALUES
('Boss-Coffee', 'NOT AGAIN FLAG{dummy_flag}');