
DROP TABLE IF EXISTS CoffeeBot;

CREATE TABLE CoffeeBot (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            description TEXT NOT NULL,
                            status TEXT NOT NULL
);

INSERT INTO CoffeeBot (name, description, status) VALUES
('Coffee', 'Classic Coffee', 'public'),
('Tee', 'To Calm you down', 'public'),
('Boss-Coffee', 'Supposed only for Bosses: FLAG{dummy_flag}', 'hidden');