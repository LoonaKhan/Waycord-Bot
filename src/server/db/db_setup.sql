create DATABASE Waycord;

USE Waycord;



-- Messages
CREATE TABLE MESSAGES(
    id INT NOT NULL UNIQUE,
    author INT NOT NULL, -- sender of the message
    contents TEXT NOT NULL, -- message contents, the text.
    attachments TEXT NOT NULL, -- this is the url to any attachments. todo: MAKE IT AN ARRAY?

    -- what channel it was sent in.
    -- we only store the id and not a channel object
    -- since we can fetch the channel from discords own db
    channel INT NOT NULL

    -- creation_time -- date created
);

-- Servers
-- in order to keep anonymity, we only store certain bits of information.
-- servers are mainly for analytics
CREATE TABLE SERVERS(
    id INT NOT NULL UNIQUE, -- make it auto increment? so that it has no connection to the server
    member_count INT NOT NULL,
    creation_date date NOT NULL, -- todo: MAYBE JUST MAKE THIS TEXT? easier to encrypt
    region VARCHAR(2) NOT NULL, -- might need to be longer
    boost_level INT NOT NULL
);

-- archive
-- contains a message + title and other info to archive
-- the main part of the app
CREATE TABLE ARCHIVES(
    id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    creator INT NOT NULL,
    message_id INT NOT NULL,
    -- creation_time -- todo: date created

    PRIMARY KEY (id),
    FOREIGN KEY (message_id) REFERENCES MESSAGES(id)
);