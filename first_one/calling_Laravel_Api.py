import json
from urllib.request import urlopen
users = {}
products={}
# import requests
#
# url = 'http://127.0.0.1:8000/api/products'
# myobj = {
# 	"name": "Khan",
# 	"description": "Not Very Pretty Looking Boy",
# 	"price": "100.1",
# 	"stock": "2",
# 	"discount":".5"
# }
#
# #use the 'auth' parameter to send requests with HTTP Basic Auth:
# #x = requests.post(url, data = myobj, auth = ('user', 'pass'))
# #use the 'headers' parameter to set the HTTP headers:
# x = requests.post(url, data = myobj, headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjZhY2YwYmYxYWI0ZWNkM2Q2NWQxZTJmYTA1ZTBhZWFjYzkxOWI2OTY1ODRhNWY0YTA0ZmJhNjg4MDEzM2RkMTRjYzEwMmU3NDRmZTcwZjA4In0.eyJhdWQiOiIyIiwianRpIjoiNmFjZjBiZjFhYjRlY2QzZDY1ZDFlMmZhMDVlMGFlYWNjOTE5YjY5NjU4NGE1ZjRhMDRmYmE2ODgwMTMzZGQxNGNjMTAyZTc0NGZlNzBmMDgiLCJpYXQiOjE1ODAwMjA0MzcsIm5iZiI6MTU4MDAyMDQzNywiZXhwIjoxNjExNjQyODM3LCJzdWIiOiIxNiIsInNjb3BlcyI6W119.YjP1CDs44nph-nRlvnzFuVdIDvdhh7Jfwy6Gg3G9dNnawl62LiRSOP_ysbo_LJaHyOehGWjyc3R1KRfC3JaCW7SWm1qfKeagGwuU1QiCGsCRY5D8wT9i4CXho1bmY3nryoptFYGL7JwhJdy_xceFabLnAP19DJSKik8OagNg3powCf3hmeH2YES4ggRZu27dz9Bde5vBOY_X3BVgC0yESkOKqIT0eVJcUesQB1a1veRcdQG5TgxaeDDD9WfEU75-ThzQgeaHkFFTd1GBIxgaphnnlTwitm7CmVMuXjePuxCl1Vz84g48dymOu7tJF3zepmoK5fuDqqFF86VHIJb2jNznK8IHodHqpLQdDwy1mh9eOdFWNOaL7GOlOLjgUTAeG7567AQuzC-BiQjy8MNd4DIJUSRcFXRwdVNKoAj6NCr3VBp9b2-UQEhV9gdZovGS9RuXzUAYtvOXu0PB1PZBsUo2JmcY-OHRL8Ujqs_lKR1fiTbXtHFK4agDX70mGdXfEaqKMLUspjcYGWH0EeBd_Klsua0DUQc7YfGlGKUuV4CGOQ2idXHB95LYrosEqA6Ikj_eawLZskQj0LD58eRcyfqtRGMqQ-ffIuo7iEbgfcS65Hd0VrRn_-Nysd7TUE-zdLYOmL82rShQCaYDM_j_8m2ZVBhnr9bCH-S0azR-SPA"})
#
# print(x.text)


#username=input("Enter Name:")
with urlopen("http://10.11.200.67:8000/api/products") as response:
      source = response.read()
      data=json.loads(source)
      users = data
      #print(users)
y = json.dumps(users)
#y=y.replace('[', '')
#y=y.replace(']', '')
#print(y)
#x="'"+y+"'"
#print(x)
#x = json.loads(y)
x = json.loads(y)
print(x)
for i in range(0,10):
 z=x['data'][i]
 #print('\t')
 print(z["name"],'-',z["totalPrice"])
# for key, value in x.items():
#     print('\t'+ key, value)


# with urlopen("http://127.0.0.1:8000/api/products") as response:
#     source = response.read()
#     data = json.loads(source)
#     products = data
#     print(products)