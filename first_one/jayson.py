import json
from urllib.request import urlopen
def github():
     users = {}
     username=input("Enter Name:")
     with urlopen("https://api.github.com/users/%s" % username) as response:
    #response = requests.get(url)
      source = response.read()
      data=json.loads(source)
      data["craeted_by"]="Abeer Azad"
      users=data
      #print(json.dumps(data,indent=3))
      #print(data["id"])
      #print(users)


      with open('user_information.json', 'w') as f:
           json.dump(data, f, indent=2)
      with open('modified_information.json', 'w') as f:
           del data['node_id']
           del data['gravatar_id']
           del data['html_url']
           del data['gists_url']
           del data['subscriptions_url']
           del data['organizations_url']
           del data['events_url']
           del data['received_events_url']
           json.dump(data, f, indent=2)
     #data = json.loads(source)
    #print(data)
     #print(json.dumps(data, indent=2))
     #print(user)

     #with open('user_information.json', 'w') as f:
     #json.load(user, f, indent=2)#
github()
