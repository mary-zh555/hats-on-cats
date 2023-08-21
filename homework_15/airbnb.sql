-- Creating tables
CREATE TABLE Hosts (
  id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
  name CHAR(60),
  budget float,
  created_at timestamp without time zone default (now() at time zone 'utc')
);

CREATE TABLE Rooms (
  id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
  host_id uuid,
  FOREIGN KEY (host_id) REFERENCES Hosts (id),
  available Boolean,
  cost_per_night float,
  amount_residents integer,
  AC Boolean,
  Refrigerator Boolean,
  created_at timestamp without time zone default (now() at time zone 'utc')
); 

CREATE TABLE Guests (
  id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
  first_name CHAR(50),
  last_name CHAR(50), 
  room_id uuid,
  FOREIGN KEY (room_id) REFERENCES Rooms (id),
  num_of_night int,
  total_fee float,
  num_of_reservations int,
  created_at timestamp without time zone default (now() at time zone 'utc')
);