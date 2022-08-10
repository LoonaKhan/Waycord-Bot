create DATABASE Waycord;

USE Waycord;



-- Messages
-- we only store the message id, author, contents and creation date.
-- these are the absolute necessities that must be preserved.
-- everything else can be accessed from discord's own db
-- this does mean that if the message is deleted, all other data will be deleted however.
CREATE TABLE MESSAGES(
    id VARCHAR(255) NOT NULL UNIQUE,
    server VARCHAR(255) NOT NULL,
    channel VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL, -- sender of the message
    contents TEXT NOT NULL, -- message contents, the text.
    creation_date TEXT NOT NULL
);

-- archive
-- contains a message + title and other info to archive
-- the main part of the app
CREATE TABLE ARCHIVES(
    id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    creator VARCHAR(255) NOT NULL,
    message_id VARCHAR(255) NOT NULL,
    creation_date TEXT NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (message_id) REFERENCES MESSAGES(id)
);
