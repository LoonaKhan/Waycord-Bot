create DATABASE Waycord;

USE Waycord;


-- Users
CREATE TABLE USERS(
  id INT NOT NULL UNIQUE , -- id's are not null because they already exist.
  name varchar(255) NOT NULL UNIQUE,
  country varchar(2) NOT NULL
);

-- Messages
CREATE TABLE MESSAGES(
    id INT NOT NULL UNIQUE ,
    author INT NOT NULL, -- sender of the message
    contents TEXT NOT NULL, -- message contents, the text.
    attachments TEXT NOT NULL, -- this is the url to any attachments. todo: MAKE IT AN ARRAY?
    channel INT NOT NULL, -- what channel it was sent in

    FOREIGN KEY (author) REFERENCES  USERS(id),
    FOREIGN KEY (channel) REFERENCES CHANNELS(id),
    PRIMARY KEY (id)
);

-- Servers
-- todo: users can see server stats, but no storing?
CREATE TABLE SERVERS(
    id INT NOT NULL UNIQUE
    -- members (array of ints?)
    -- member count?
    -- creation date?
    -- server location
    -- icon url
    -- boost level
    -- name
);

-- Channels?
-- todo: is there even a point in having this?
CREATE TABLE CHANNELS(
    id INT NOT NULL UNIQUE ,
    name VARCHAR(255)
);

-- emojis?
CREATE TABLE EMOJIS(
    id INT NOT NULL UNIQUE ,
    name VARCHAR(255) NOT NULL,
    image_url VARCHAR(255) NOT NULL
);
