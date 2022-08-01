"""
Wrapper for the API

The bot will need to call on the api/db for data instead of storing it locally.
When it does, these methods will be used.

dev: lvlonEmperor
date: July 28 2022
"""

import sys
import requests as req
import json

port = 4000
base_url = f"http://localhost:{port}/"
message_url = base_url + "messages/"
archive_url = base_url + "archives/"



#  Messages calls
def getMsg(key:str, id:int):
    res = req.get(url=message_url + f"{id}",
                  headers={
                      "key": key
                  })
    return json.loads(res.text)

def addMsg(key:str, id:int, author:int, contents:str, channel:int, creation_date:str):
    res = req.post(url=message_url,
                  headers={
                      "key": key
                  },
                  data={
                      "id": id,
                      "author": author,
                      "contents": contents,
                      "channel": channel,
                      "creation_date": creation_date
                  })
    return json.loads(res.text)

def delMsg(key:str, id:int):
    res = req.delete(url=message_url + f"{id}",
                     headers={
                         "key": key
                     })
    return json.loads(res.text)



# Archives calls
def getUserArchivesByTitle(key:str, creator_id:int, title:str):
    res = req.get(url=archive_url + f"{creator_id}/filter",
                  headers={
                      "key": key
                  },
                  data={
                      "title": title
                  })
    return json.loads(res.text)

def getUserArchives(key:str, creator_id:int):
    res = req.get(url=archive_url + f"{creator_id}",
                  headers={
                      "key": key
                  })
    return json.loads(res.text)

def addArchive(key:str, creator_id:int, title:str, message_id:int, creation_date:str):
    res= req.post(url=archive_url,
                  headers={
                      "key": key
                  },
                  data={
                      "creator_id": creator_id,
                      "title": title,
                      "message_id": message_id,
                      "creation_date": creation_date
                  })
    return json.loads(res.text)

def delArchive(key:str, id:int):
    res = req.delete(url=archive_url + f"{id}",
                     headers={
                         "key": key
                     })
    return json.loads(res.text)



if __name__ == '__main__': # tests
    # Key test
    #print(getMsg(key="key", id=1)) # wrong key. dosent run

    # getMsg tests
    #print(getMsg(key="key", id=-1)) # proper, runs
    #print(getMsg(key="key", id="g")) # wrong type or non-existent id, just dosent return a message

    # addMsg tests
    #print(addMsg(key="key", id=-3, author=372, contents="", channel=100, creation_date="today")) # proper
    #print(addMsg(key="key", id=-4, author=372, contents="f", channel=100, creation_date="today")) # id already exists
    # invalid type: id, author, contents, channel and creation date. only dosent run when integer fields are not ints
    # the only user-given field here is id. and archives already validates it
    #print(addMsg(key="key", id=-6, author=372, contents="", channel=100, creation_date="today"))

    # getUserArchivesByTitle test
    #print(getUserArchivesByTitle(key="key", creator_id=2, title="")) # proper
    #print(getUserArchivesByTitle(key="key", creator_id=3, title=""))# creator dosent exits. runs but returns empty
    #print(getUserArchivesByTitle(key="key", creator_id=1, title="z"))# title doesnt match. runs but empty array

    # getUserArchives test
    #print(getUserArchives(key="key", creator_id=2)) # proper
    #print(getUserArchives(key="key", creator_id=3))# dosent exist. runs but empty array

    # addArchive test
    #print(addArchive(key="key", creator_id=1, title="lol", message_id=-1, creation_date="idk")) # proper
    #print(addArchive(key="key", creator_id=1, title="lol", message_id=-100, creation_date="idk")) # message does not exist

    sys.exit()



