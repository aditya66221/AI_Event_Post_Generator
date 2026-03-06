CREATE DATABASE ai_events;

USE ai_events;

-- Table to store events
CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    date DATE,
    location VARCHAR(255),
    type VARCHAR(100),
    description TEXT
);

-- Table to store generated posts
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    platform VARCHAR(50),
    content TEXT,
    status VARCHAR(50),
    FOREIGN KEY (event_id) REFERENCES events(id)
);