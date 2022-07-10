# Database Docs
The main objects stored in the database are Messages, Archives and Servers.

The database will likely be hosted using mysql over mariadb if that is easier to dockerize


## Messages:
Messages are comprised of:
- id: message id
- author: id of the user who sent the message
- contents: the text of the message 
- attachments: url's any files sent with the message
- channel: id of the channel the message was sent in.
- creation_time: datetime the message was created

Messages only store what discord already stores. the only user data collected is the user id.
Anything else the app will need concerning the user can be fetched via id and the discord API, but will not be stored.
There are actually no references to other db tables(author or channel referencing a user or channel table)
because there simply arent any db objects for those and so little information is needed to store the message date.



## Archives:
Archives are comprised of:
- id: id of the archive
- title: name of the archive
- creator: id of the user who created the archive
- message_id: id of the message being archived
- creation_time: datetime the message was created


    
## Servers:
Servers are comprised of:
- id: id of the server
- member_count: the number of users in a server
- creation_date: when the server was created
- region: the region the server is in (American-East, Europe etc)
- boost_level: what boost level the server is at

Server data is stored only for potential analytics one day.
any and all personal data about a server is not stored and allows for near-complete anonymity.

Examples:
- member_count simply has the number of members, but cannot say WHO is in the server or anything about them.

Exceptions are region, however, that is rather insignificant and is not necessarily representative of the users of 
said server. Additionally, id needs to be tied to the server id so that we can identify it

TODO: some servers can be blacklisted, so have a blacklisted server table?
