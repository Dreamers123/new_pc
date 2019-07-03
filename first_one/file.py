from urllib.request import urlopen
import json
with open("user_information.json", "r") as rf:
    with open("user_information.txt", "w") as wf:
     for line in rf:
      wf.write(line)
with open("user_information.json", "r") as rif:
     getit=rif.read()
     data = json.loads(getit)
     print(data['avatar_url'])
     #img=getit['avatar_url']
     with urlopen(data['avatar_url']) as response:
         with open("bronx_copy.jpg", "wb") as wf:
          for line in response:
           wf.write(line)