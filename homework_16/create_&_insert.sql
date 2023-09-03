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


---- hosts.csv
insert into hosts (name, budget)
values 
	('Sunset Oasis Resort', 50000),
	('Grand Skyline Hotel', 150000),
	('Tranquil Haven Inn', 10000);


---- rooms.csv
insert into rooms (host_id, available, cost_per_night, amount_residents, ac, refrigerator)
values 
    ('0857ee00-2040-4bb0-940d-b6ec4d5143bd', true, 120.50, 2, true, true),
	('caff3719-ed5f-414c-bc62-bca6cfb04539', false, 85.00, 1, false, true),
	('fb32c0ac-3844-4e89-9bcb-fc10754a1a33', true, 150.75, 3, true, false),
	('0857ee00-2040-4bb0-940d-b6ec4d5143bd', false, 50, 2, false, false),
	('0857ee00-2040-4bb0-940d-b6ec4d5143bd', true, 200, 5, true, true);


---- rooms_hosts_join.csv
SELECT
    r.id,
    r.host_id,
    h.name AS host_name,
    r.available,
    r.cost_per_night,
	r.amount_residents
FROM Rooms r
JOIN Hosts h ON r.host_id = h.id;


-- Function to calculate total_fee
CREATE OR REPLACE FUNCTION calculate_total_fee()
RETURNS TRIGGER AS $$
BEGIN
  NEW.total_fee = NEW.num_of_night * (
    SELECT cost_per_night
    FROM Rooms
    WHERE id = NEW.room_id
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER calculate_total_fee_trigger
BEFORE INSERT ON Guests
FOR EACH ROW
EXECUTE FUNCTION calculate_total_fee();


---- guests.csv
INSERT INTO Guests
(first_name, last_name, room_id, num_of_night, num_of_reservations)
VALUES 
('John', 'Doe', '3082bb0b-978f-4363-86ca-6de7d3b5334a', 5,  2),
('Jane', 'Smith', 'aa632b74-f701-4976-b866-bd13773165f5', 3, 1),
('Michael', 'Johnson', '334d17d1-b2cd-435e-a8b4-5c683b53d6bf', 7, 3);
