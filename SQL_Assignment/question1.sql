/* creating a table called user */
CREATE TABLE IF NOT EXISTS User (
    id Primary Key Auto,
    Username VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP CURRENT_TIMESTAMP
);

SHOW TABLES;

/* Insert sample data into the table */
INSERT INTO Users (username, email, created_at)
VALUES 
('ama', 'ama@example.com',;2024-11-01 10:30:00),
('Abena', 'abena@example.com', 2024-11-02 12:00:00),
('adjoa', 'adjoa@example.com', 2024-11-03 14:15:00);
