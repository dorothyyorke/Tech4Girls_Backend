/* creating a table called user */
CREATE TABLE IF NOT EXISTS User (
    id Primary Key Auto,
    Username VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP CURRENT_TIMESTAMP
    FOREIGN KEY (user_id) REFERENCES usre(id) ON DELETE CASCADE 
);

SHOW TABLES;

--inserting data into post table to establish a one-to many relationship 
INSERT INTO posts (user_id, title, content, created_at)
VALUES (1, 'first post', 'content of ama', '2024-11-01 10:45:00'),
       (1, 'second post', 'more content from ama', '2024-11-01 11:30:00'),
       (2, 'first post', 'content of abena', '2024-11-02 12:45:00'),
       (3, 'first post', 'content of adjoa', '2024-11-03 14:20:00');