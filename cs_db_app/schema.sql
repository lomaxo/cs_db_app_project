DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS item;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE item (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  description varchar(100) NOT NULL,
  location_id varchar(10)
);