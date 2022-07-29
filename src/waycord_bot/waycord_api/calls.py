"""
All the api calls to the server.

The bot will need to call on the server/db for data instead of storing it locally.
When it does, these methods will be used.
This doubles as a wrapper for the API

dev: lvlonEmperor
date: July 28 2022

todo:
    make it several specialized methods.
    maybe merge add and delete methods into one?
    test SQL injections

"""

import requests as req
import json

port = 4000
base_url = f"http://localhost:{port}/"
server_url = base_url + "servers/"
message_url = base_url + "messages/"
archive_url = base_url + "archives/"

def call(type, url, headers={}, params={}, data={}):
    # general api call
    # in python data is the same thing as body
    res = req.request(method=type, url=url, headers=headers, params=params, data=data)
    return json.loads(res.text)



# Server calls
def getServer(key:str, id:int):
    # gets a server by ID
    res = req.get(url=server_url+ f"{id}",
                  headers={
                      "key": key
                  })
    return json.loads(res.text)

def addServer(key:str, member_count:int, creation_date:str, boost_level:int):
    # adds a new server based on info given
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
    # updates a server based on the info given
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
    # deletes a server by id
    res = req.delete(url=server_url + f"{id}",
                     headers={
                         "key": key
                     })
    return json.loads(res.text)


#  Messages calls
def getMsg(): pass

def addMsg(): pass

def delMsg(key:str, id:int):
    res = req.delete(url=message_url + f"{id}",
                     headers={
                         "key": key
                     })
    return json.loads(res.text)



# Archives calls
def getUserArchivesByTitle(): pass

def getUserArchives(): pass

def addArchive(): pass

def delArchive(key:str, id:int):
    res = req.delete(url=archive_url + f"{id}",
                     headers={
                         "key": key
                     })
    return json.loads(res.text)



if __name__ == '__main__': # tests

    """ call()
    print(call(type="GET",
               url="http://localhost:4000/messages/-4", # put params in the url
               headers={"key":"key"}
            ))
    """


    # getServer tests
    # print(getServer(key="hkey", id=1)) # wrong key. dosent run
    # print(getServer(key="key", id=-1)) # nonexistent id. dosent run
    # print(getServer(key="key", id=3)) # proper key and id. runs


    # addServer

    # proper. runs
    #print(addServer(key="key", member_count=0, creation_date="sometime", boost_level=2))
    # wrong key. dosent run
    #print(addServer(key="hkey", member_count=0, creation_date="sometime", boost_level=2))
    # negative values. runs
    #print(addServer(key="key", member_count=-1, creation_date="sometime", boost_level=-1))
    # bad type. runs
    #print(addServer(key="key", member_count=0, creation_date=1, boost_level=2))
    # bad type: "0". runs since JS converts it automatically
    #print(addServer(key="key", member_count="0", creation_date="sometime", boost_level=2))
    # bad type: "l". dosent run since JS cant convert "l" to a number
    #print(addServer(key="key", member_count="l", creation_date="sometime", boost_level=2))


    # delServer
    #print(delServer(key="key", id=12)) # proper
    #print(delServer(key="kehy", id=10)) # wrong id. dosent run
    #print(delServer(key="key", id=-10)) # non-existant id. runs, but nothing happens

    # updateServer
    #print(updateServer(key="key", id=9, member_count=10, boost_level=0)) # proper
    #print(updateServer(key="keyy", id=9, member_count=10, boost_level=0)) # invalid key. dosent run
    #print(updateServer(key="key", id=1, member_count=10, boost_level=0)) # invalid id. runs, but dosent do anything
    #print(updateServer(key="key", id=9, member_count=10, boost_level="g")) # invalid type "g". dosent run
    #print(updateServer(key="key", id=9, member_count=11, boost_level="0")) # invalid type. runs because JS
