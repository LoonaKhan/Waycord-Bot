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
server_url = base_url + "servers/"
message_url = base_url + "messages/"
archive_url = base_url + "archives/"



# Server calls
def getServer(key:str, id:int):
    # gets a api by ID
    res = req.get(url=server_url+ f"{id}",
                  headers={
                      "key": key
                  })
    return json.loads(res.text)

def addServer(key:str, member_count:int, creation_date:str, boost_level:int):
    # adds a new api based on info given
    res = req.post(url=server_url,
                   headers={
                       "key": key
                   },
                   data={
                       "member_count": member_count,
                       "creation_date": creation_date,
                       "boost_level": boost_level
                   })
    return json.loads(res.text)

def updateServer(key:str, id:int, member_count:int, boost_level:int):
    # updates a api based on the info given
    res = req.put(url=server_url + f"{id}",
                  headers={
                      "key": key
                  },
                  data={
                      "member_count": member_count,
                      "boost_level": boost_level
                  })
    return json.loads(res.text)

def delServer(key:str, id:int):
    # deletes a api by id
    res = req.delete(url=server_url + f"{id}",
                     headers={
                         "key": key
                     })
    return json.loads(res.text)


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

    # getServer tests
    # print(getServer(key="key", id=-1)) # nonexistent id. dosent run
    # print(getServer(key="key", id=3)) # proper key and id. runs


    # addServer
    # Bad types here are fine since the user cannot interact with the servers

    # proper. runs
    #print(addServer(key="key", member_count=0, creation_date="sometime", boost_level=2))
    # bad creation_date type. runs. but this is fine since the user cannot edit this
    #print(addServer(key="key", member_count=0, creation_date=1, boost_level=2))
    # bad member_count type: "0". runs since JS converts it automatically
    #print(addServer(key="key", member_count="0", creation_date="sometime", boost_level=2))
    # bad member_count type: "l". dosent run since JS cant convert "l" to a number
    #print(addServer(key="key", member_count="l", creation_date="sometime", boost_level=2))


    # delServer
    # because all delete methods are the same, no other tests will be kept
    #print(delServer(key="key", id=12)) # proper
    #print(delServer(key="key", id=-10)) # non-existant id. runs, but nothing happens

    # updateServer
    #print(updateServer(key="key", id=9, member_count=10, boost_level=0)) # proper
    #print(updateServer(key="key", id=1, member_count=10, boost_level=0)) # invalid id. runs, but dosent do anything
    #print(updateServer(key="key", id=9, member_count=10, boost_level="g")) # invalid type "g". dosent run
    #print(updateServer(key="key", id=9, member_count=11, boost_level="0")) # invalid type. runs because JS


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



