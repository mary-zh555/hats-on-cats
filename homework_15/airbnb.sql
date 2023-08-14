CREATE TABLE `Users` (
  `id` uuid PRIMARY KEY,
  `type` char,
  `created_at` timestamp
);

CREATE TABLE `Hosts` (
  `host_id` uuid PRIMARY KEY,
  `created_at` timestamp
);

CREATE TABLE `Guests` (
  `guest_id` uuid PRIMARY KEY,
  `room_id` uuid,
  `created_at` timestamp
);

CREATE TABLE `Rooms` (
  `id` uuid PRIMARY KEY,
  `host_id` uuid,
  `available` Boolean,
  `amount_residents` integer,
  `price` float,
  `AC` Boolean,
  `Refrigirator` Boolean,
  `created_at` timestamp
);

ALTER TABLE `Hosts` ADD FOREIGN KEY (`host_id`) REFERENCES `Rooms` (`host_id`);

ALTER TABLE `Hosts` ADD FOREIGN KEY (`host_id`) REFERENCES `Users` (`id`);

ALTER TABLE `Guests` ADD FOREIGN KEY (`guest_id`) REFERENCES `Users` (`id`);

ALTER TABLE `Rooms` ADD FOREIGN KEY (`id`) REFERENCES `Guests` (`room_id`);
