-- Створення таблиці sensors_coordinates
CREATE TABLE IF NOT EXISTS sensors_coordinates (
    sensor_id INT NOT NULL,
    coordinate_id INT NOT NULL,
    PRIMARY KEY (sensor_id, coordinate_id),
    FOREIGN KEY (sensor_id) REFERENCES sensors(id),
    FOREIGN KEY (coordinate_id) REFERENCES coordinates(id)
); 