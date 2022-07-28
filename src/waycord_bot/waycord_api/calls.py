"""
All the api calls to the server.

The bot will need to call on the server/db for data instead of storing it locally.
When it does, these methods will be used.

dev: lvlonEmperor
date: July 28 2022

todo:
    make it several specialized methods.
    maybe merge add and delete methods into one?

"""

import requests as req
import json

base_url = ""

def call(type, url, headers={}, params={}, data={}):
    # general api call
    # in python data is the same thing as body
    res = req.request(method=type, url=url, headers=headers, params=params, data=data)
    return json.loads(res.text)



# Server calls
def getServer(): pass

def addServer(): pass

def updateServer(): pass

def delServer(): pass


#  Messages calls
def getMsg(): pass

def addMsg(): pass

def delMsg(): pass



# Archives calls
def getUserArchivesByTitle(): pass

def getUserArchives(): pass

def addArchive(): pass

def delArchive(): pass



if __name__ == '__main__':

    print(call(type="GET",
               url="http://localhost:4000/messages/-4", # put params in the url
               headers={"key":"key"}
            ))
