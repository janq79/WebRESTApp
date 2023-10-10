USE mydb;

CREATE TABLE IF NOT EXISTS users (
    user_id INT NOT NULL PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    creation_date DATETIME NOT NULL
);

INSERT INTO users (user_id, user_name, creation_date) VALUES (1, 'Jan Kowalski', NOW());
INSERT INTO users (user_id, user_name, creation_date) VALUES (2, 'Anna Nowak', NOW());