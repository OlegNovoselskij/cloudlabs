-- Додавання локацій
INSERT INTO locations (country, street) VALUES
('Ukraine', 'Shevchenka 1'),
('Ukraine', 'Franka 15'),
('Poland', 'Warszawska 10');

-- Додавання користувачів
INSERT INTO users (username, email, password_hash, role) VALUES
('admin', 'admin@example.com', 'hashed_password_1', 'admin'),
('user1', 'user1@example.com', 'hashed_password_2', 'user');

-- Додавання клієнтів
INSERT INTO customers (name, email, phone, location_id) VALUES
('Customer 1', 'customer1@example.com', '+380501234567', 1),
('Customer 2', 'customer2@example.com', '+380502345678', 2);

-- Додавання насосів
INSERT INTO pumps (capacity, location_id) VALUES
(100.5, 1),
(150.75, 2),
(200.0, 3);

-- Додавання операцій насосів
INSERT INTO pumpOperations (end_time, water_pumped, pump_id) VALUES
('2024-03-20 11:00:00', 50.25, 1),
('2024-03-20 13:00:00', 75.5, 2);

-- Додавання типів сенсорів
INSERT INTO sensor_types (id, name, description) VALUES
(1, 'Temperature', 'Measures temperature'),
(2, 'Pressure', 'Measures pressure'),
(3, 'Humidity', 'Measures humidity');

-- Додавання сенсорів
INSERT INTO sensors (installation_date, type_id) VALUES
('2024-01-01', 1),
('2024-01-02', 2),
('2024-01-03', 3),
('2024-01-04', 1),
('2024-01-05', 2);

-- Додавання координат
INSERT INTO coordinates (latitude, longitude) VALUES
(50.4501, 30.5234),
(50.4502, 30.5235),
(50.4503, 30.5236),
(50.4504, 30.5237),
(50.4505, 30.5238);

-- Додавання сопел
INSERT INTO sopla (max_water_dlow, location_id, coordinate_id) VALUES
(80.5, 1, 1),
(120.75, 2, 2);

-- Додавання зв'язків сенсорів з координатами
INSERT INTO sensors_coordinates (sensor_id, coordinate_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- Додавання показань сенсорів
INSERT INTO sensor_readings (timestamp, value, unit, sensor_id) VALUES
('2024-01-01 10:00:00', 25.5, '°C', 1),
('2024-01-01 10:00:00', 60.0, 'kPa', 2),
('2024-01-01 10:00:00', 1013.2, '%', 3),
('2024-01-01 10:00:00', 500.0, '°C', 4),
('2024-01-01 10:00:00', 1.0, 'kPa', 5); 