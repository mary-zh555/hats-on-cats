CREATE TABLE Hosts (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name CHAR(60),
  budget FLOAT,
  average_rating FLOAT,
  created_at TIMESTAMP without time zone default (now() at time zone 'utc')
);

CREATE TABLE Rooms (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  host_id uuid,
  FOREIGN KEY (host_id) REFERENCES Hosts(id)
  available BOOLEAN,
  cost_per_night FLOAT,
  amount_residents INTEGER,
  AC BOOLEAN,
  Refrigerator BOOLEAN,
  created_at TIMESTAMP without time zone default (now() at time zone 'utc')
);

CREATE TABLE Guests (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  first_name CHAR(50),
  last_name CHAR(50),
  num_of_reservations INT,
  created_at TIMESTAMP without time zone default (now() at time zone 'utc')
);

CREATE TABLE Reservation (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  guest_id uuid,
  room_id uuid,  
  FOREIGN KEY (guest_id) REFERENCES Guests(id),
  FOREIGN KEY (room_id) REFERENCES Rooms(id),
  payment_status BOOLEAN,
  total_fee FLOAT,
  check_in_date TIMESTAMP,
  check_out_date TIMESTAMP,
  num_of_night INT,
  created_at TIMESTAMP without time zone default (now() at time zone 'utc')
);

CREATE TABLE Review (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  guest_id uuid,
  host_id uuid,
  FOREIGN KEY (guest_id) REFERENCES Guests(id),
  FOREIGN KEY (host_id) REFERENCES Hosts(id),
  ratings INT,
  comment CHAR(200),
  created_at TIMESTAMP without time zone default (now() at time zone 'utc')
);