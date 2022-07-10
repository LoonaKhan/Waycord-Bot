# Server docs
This lists all the API endpoints and their explanations.



## Servers:
Servers are mainly used for server commands. general information about the server you are in.
The data stored in a server is a lot less than what might be shown to the user as most of it is not stored.

### Fetch a server
``GET (base_url)/:id``
- give the server id, return the server object.
- this command may be obsolete

### Add a server
``POST (base_url)/:id``
- give the server id, create a server object.
- used when the bot first joins a server, or when its called.

### Update a server
``PUT (base_url)/:id``
- give the server id, update the server object.
- used whenever a server-related command is called

### Delete a server
``DELETE (base_url)/:id``
- give the server id, delete the server object.
- this is used if the admins of a server wish to prevent the server from being tracked



## Messages:
- get one. for archives. cant we just do joins?
- add a message. whenver we create an archive
- delete a message. whenever we unarchive


## Archives
- get an archive. user wishes to view their own archives. cannot view others. can search by name or creation date?
- create an archive
- delete an archive