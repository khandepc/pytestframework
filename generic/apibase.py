import requests as req
import json

url='http://localhost:9515/session'
data=json.dumps({
    "desiredCapabilities": {
        "caps": {
            "nativeEvents": "false",
            "browserName": "chrome",
            "version": "",
            "platform": "ANY"
        }
    }
})
r=req.post(url,data)


# req.delete('http://localhost:9515/session/1edf41f715a2dbccf6ea7216bfa13998')
#req.post()
# print(r.json())
# r = req.get('http://google.com')
# r.url

class ApiBase:
    pass