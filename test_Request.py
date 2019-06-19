import requests
baseUrl='https://reqres.in'
uri='/api/users'
params={'page':2}
data=requests.get(baseUrl+uri,params)
data_dict=data.json()
#print(data_dict)
for item in data_dict['data']:
    print('id:'item['id'])
    print('Name:' item['first_name']+' '+item['last_name'])
    
    print(' ')
    

    
