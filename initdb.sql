CREATE DATABASE gascheck;
CREATE USER gascheck WITH PASSWORD 'gascheck';
GRANT ALL PRIVILEGES ON DATABASE gascheck to gascheck;

CREATE TABLE pricecheck (
    station_id varchar(40) NOT NULL,
    ts timestamp DEFAULT NOW(),
    type varchar(10) NOT NULL,
    price numeric(6,4),
);

CREATE TABLE station (
    station_id varchar(40) NOT NULL,
    brandname varchar(40),
    city varchar(40),
    street varchar(40),
    streetno varchar(40)
    last_checked_ts timestamp
);

ALTER TABLE station ADD PRIMARY KEY (station_id);

ALTER TABLE pricecheck ADD CONSTRAINT fk_station_id FOREIGN KEY (station_id) REFERENCES station ON DELETE CASCADE;
