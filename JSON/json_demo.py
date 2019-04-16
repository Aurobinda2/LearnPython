import json

string1='''{
            "people" : [
            {
            "name":"Aurobinda",
            "phone":"+91-9673894649",
            "emails": ["aurobinda.nayak783@gmail.com", "aurobindr.nayak3@gmail.com"],
            "has_license":false
            },
           {
            "name": "Rajesh",
            "phone": "+91-9673898971",
            "emails": ["Rajesh.nayak783@gmail.com", "Raju123.nayak3@gmail.com"],
            "has_license":true
            }
        ]

    }'''

#Convert json object to <dict> data
data=json.loads(string1)
for d in data['people']:
    #print (d['name'])
    d['phone']="09673894649"
    #print(d['phone'])
json_data=json.dumps(data,indent=2,sort_keys=True)

with open("C:/Users/au332045/PycharmProjects/Json/Dummy_jsondata.json","w") as f:
    f.write(json_data)

