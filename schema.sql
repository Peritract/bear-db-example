DROP DATABASE bear_attacks;
CREATE DATABASE bear_attacks;
\c bear_attacks;

CREATE TABLE bear_type (
    bear_type_id INT GENERATED ALWAYS AS IDENTITY,
    bear_type VARCHAR(10),
    PRIMARY KEY (bear_type_id)
);

CREATE TABLE location (
    location_id INT GENERATED ALWAYS AS IDENTITY,
    location_name VARCHAR(20),
    PRIMARY KEY (location_id)
);

CREATE TABLE bear_attack (
    bear_attack_id INT GENERATED ALWAYS AS IDENTITY,
    bear_type_id INT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    location_id INT NOT NULL,
    PRIMARY KEY (bear_attack_id),
    FOREIGN KEY (bear_type_id) REFERENCES bear_type (bear_type_id),
    FOREIGN KEY (location_id) REFERENCES location (location_id)
);