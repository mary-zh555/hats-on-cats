CREATE TABLE Users (
  id serial PRIMARY KEY,
  user_type CHAR,
  created_at timestamp
);

CREATE TABLE Hosts (
  id serial,
  FOREIGN KEY (id) REFERENCES Users (id),
  created_at timestamp
);

CREATE TABLE Guests (
  id serial,
  room_id serial,
  FOREIGN KEY (id) REFERENCES Users (id), (room_id) REFERENCES Rooms (id),
  created_at timestamp
);

CREATE TABLE Rooms (
  id serial PRIMARY KEY,
  host_id serial,
  FOREIGN KEY (host_id) REFERENCES Hosts (id),
  available Boolean,
  amount_residents integer,
  price float,
  AC Boolean,
  Refrigerator Boolean,
  created_at timestamp
);
