import os
import json
import time
import requests

webhook=os.environ["WEBHOOK"]
content=os.environ["CONTENT"]
mobile=os.environ["MOBILE"]

header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
            }
text ={
    "content": content,
    "mentioned_list":['@all']
}
if len(mobile)>10:
    text ={
        "content": content,
        "mentioned_mobile_list":[mobile]
    }
data ={
    "msgtype": "text",
    "text": text
}
data = json.dumps(data)
info = requests.post(url=webhook, data=data, headers=header)
