#! /usr/bin/env python3
import os
import requests



for f in os.listdir("/data/feedback/"):
  with open("/data/feedback/"+f,"r") as file:
    line=file.read().splitlines() 
    p={"title":str(line[0]) ,
    "name":str(line[1]) ,
    "date":str(line[2]),
    "feedback":str(line[3])   
    }
    print(p)
    response = requests.post("http://34.70.227.213/feedback/",json=p)
    print(response.headers.keys())
    print(response.status_code)

