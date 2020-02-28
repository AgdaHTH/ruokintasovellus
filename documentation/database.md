![alt text][picture]

[picture]: https://github.com/AgdaHTH/ruokintasovellus/blob/master/documentation/database.png

    CREATE TABLE food (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        price INTEGER,
        PRIMARY KEY (id),
        UNIQUE (name))

    CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id))

    CREATE TABLE animal (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        sick BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        CHECK (sick IN (0, 1)))

    CREATE TABLE animalsfoods (
        animal_id INTEGER,
        food_id INTEGER,
        FOREIGN KEY(animal_id) REFERENCES animal (id),
        FOREIGN KEY(food_id) REFERENCES food (id))
