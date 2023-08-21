-- Find a user who had the biggest amount of reservations. Return username and user_id

SELECT id, first_name, last_name
FROM Guests
WHERE num_of_reservations = (
  SELECT MAX(num_of_reservations)
  FROM Guests
);
-- "17a70d8a-48ff-4e1d-9b6a-3d66b8b2ceb3"	"Michael" 