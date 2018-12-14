CREATE TABLE IF NOT EXISTS guest (
    no integer PRIMARY KEY autoincrement,
    title string NOT NULL,
    content string NOT NULL,
    writer string NOT NULL,
    regdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);